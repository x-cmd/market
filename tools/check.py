import os,re,glob,yaml,json,subprocess,sys,urllib.request,urllib.parse

NET = '--net' in sys.argv
ROOT='/Users/l/.x-repo/github.com/x-cmd/market'
os.chdir(ROOT)
BAN=['底层驱动','底层逻辑','值得注意的是','综上','总体来看','机制','框架','维度','抓手','从而','进行','方面',
     '应该','建议','策略','打法','增长黑客']
# 站里已规划但还没写的页面：链过去是正常的，只要目标在 OUTLINE 里声明过
OUT=yaml.safe_load(open('OUTLINE.yml'))
PLANNED={f"{s['id']}/{a['id']}" for s in OUT['series'] for a in s['articles']}
fail=0
for f in sorted(glob.glob('docs/**/*.md',recursive=True)):
    t=open(f).read()
    print(f'\n=== {f} ===')
    # 结构
    h1=re.findall(r'^# .+',t,re.M); h2=re.findall(r'^## .+',t,re.M); h3=re.findall(r'^### .+',t,re.M)
    numbered=[x for x in re.findall(r'^#{2,3} .+',t,re.M) if re.match(r'^#+\s*(Lens|Case|角度|\d+[ ·.])',x)]
    ok = len(h1)==1 and not numbered
    print(f'  H1={len(h1)} H2={len(h2)} H3={len(h3)} 编号式小标题{len(numbered)}', '✓' if ok else '✗ 结构违规'); fail+= (not ok)
    # 字数
    body=re.sub(r'```.*?```','',t,flags=re.S); body=re.sub(r'<[^>]+>','',body)
    bb=re.sub(r'<a href.*?</a>','',body,flags=re.S)
    bb=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',bb)
    han=len(re.sub(r'\s','',re.sub(r'[*`]','',bb)))
    print(f'  字数 {han}', '✓' if 2000<=han<=3000 else ('△ 偏短' if han<2000 else '△ 偏长'))
    # 开头不编画面：前 300 字里不出现具体时刻
    head=re.sub(r'\s','',body)[:300]
    stage=[w for w in ['周一','周二','周三','周四','周五','早上','晚上','凌晨','十点','九点','八点'] if w in head]
    print(f'  开头编画面 {stage if stage else "无 ✓"}'); fail+=bool(stage)
    # 禁用词
    hit=[w for w in BAN if w in body]
    print(f'  禁用词 {hit if hit else "无 ✓"}'); fail+=bool(hit)
    # 长句
    sents=[s for s in re.split(r'[。！？\n]',body) if len(re.findall(r'[一-鿿]',s))>0]
    longs=[s.strip()[:60] for s in sents if len(re.findall(r'[一-鿿]',s))>60]
    print(f'  >60字长句 {len(longs)}', longs[:2] if longs else '✓')
    # 分号串从句
    sc=body.count('；'); print(f'  分号 {sc}', '✓' if sc<=2 else '△')
    # Python 列表字面量漏进正文：写表时把整张表存成 ['| a | b |', ...] 贴了进来
    leak=[l for l in t.split('\n') if re.match(r"^\s*\[\s*['\"]",l)]
    print(f'  列表字面量漏出 {len(leak)}', (leak[0].strip()[:60] if leak else '无 ✓')); fail+=bool(leak)
    # markdown 表格：表头后面要紧跟分隔行，整张表列数一致
    tl=re.findall(r'^\|.*$',body,re.M)
    badtab=[]; ntab=0; i=0
    while i < len(tl):
        if re.match(r'^\|[\s:\-|]+\|$',tl[i]) and i>0 and re.match(r'^\|.*\|$',tl[i-1]):
            ntab+=1
            hdr=tl[i-1]; n=hdr.count('|')
            if n!=tl[i].count('|'): badtab.append(f'表头与分隔行列数不同: {hdr[:40]}')
            j=i+1
            while j<len(tl) and tl[j].count('|')==n: j+=1
            # 走到下一个表头（后头跟分隔行）是正常的，那是下一张表
            if j<len(tl) and tl[j].startswith('|') and not (j+1<len(tl) and re.match(r'^\|[\s:\-|]+\|$',tl[j+1])):
                badtab.append(f'列数不齐: {tl[j][:40]}')
            i=j
        else:
            i+=1
    print(f'  表格 {ntab} 张', (badtab[:2] if badtab else '✓')); fail+=bool(badtab)
    # 链接：能落地，或指向 OUTLINE 里已规划的页面
    bad=[]
    for m in re.finditer(r'\]\(([^)]+)\)',t):
        l=m.group(1)
        if l.startswith(('http','#')): continue
        target=os.path.normpath(os.path.join(os.path.dirname(f),l.split('#')[0]))
        if os.path.exists(target): continue
        # 目标是不是站里已声明但还没写的页面
        rel=os.path.relpath(target,os.path.join(ROOT,'docs'))
        if rel.endswith('/cn.md'): rel=rel[:-len('/cn.md')]
        if rel in PLANNED: continue
        bad.append(l)
    print(f'  相对链接 {bad if bad else "全部可解析 ✓"}'); fail+=bool(bad)
    # 图：这张主机偶尔慢，20 秒会误报失败，所以重试几次再判
    urls=re.findall(r'https://x-cmd\.com/draw/(?:echarts|archmap|mindmap)\?[^\s"\)]+',t)
    urls=[u for u in urls if '/explore/' not in u]
    print(f'  图 {len(urls)} 张' + ('' if NET else '（加 --net 逐张验活）'))
    if NET:
        for full in urls:
            code=''; svg=''
            for _ in range(3):
                code=subprocess.run(['curl','-s','-o','/tmp/_v.svg','-w','%{http_code}','--max-time','20',full],capture_output=True,text=True).stdout
                svg=open('/tmp/_v.svg',errors='ignore').read()
                if code=='200' and ('<metadata>' in svg or '<svg' in svg): break
            ok = code=='200' and ('<metadata>' in svg or '<svg' in svg)
            print(f'    HTTP {code} svg={len(svg)}B {"OK" if ok else "BAD"}'); fail+= not ok
    # 复现命令：只有写成反引号包着的命令行才真跑
    m=re.search(r'\*\*复现\*\*：(.+)',t)
    if m:
        raw=m.group(1).strip()
        cm=re.search(r'`([^`]+)`',raw)
        if not cm:
            print(f'  复现说明 {raw[:60]} → ✓ (非命令行)')
        else:
            cmd=cm.group(1).strip()
            c=subprocess.run(['zsh','-c',cmd+' 2>&1 | head -3'],capture_output=True,text=True)
            ok='E|' not in c.stdout and 'error' not in c.stdout.lower()
            print(f'  复现命令 {cmd[:70]} → {"✓" if ok else "△"}')
            print('    ', c.stdout.strip().splitlines()[:3])
for f in sorted(glob.glob('docs/*/*/faq.yml')):
    d=yaml.safe_load(open(f))
    print(f'\n=== {f} ===')
    print('  id:', d['id'], '✓' if d['id']=="x-market-"+"-".join(f.split('/')[1:3]) else '✗')
    total=0
    for s in d['data']:
        for qa in s['qa']:
            total+=1
            assert set(qa['question'])=={'en','cn'}, qa['id']
            assert set(qa['answer'])=={'en','cn'}, qa['id']
            assert 0<=qa['confidence']<=10
            for r in qa['reference']: assert os.path.exists(r), r
    print(f"  {total} 条 QA（{len(d['data'])} 组）· en/cn 齐全 ✓ · reference 路径存在 ✓")

# ── spec 页与口径卡：互相引用的都得在 ─────────────────────────────
print('\n=== spec 页 / 口径卡 交叉引用 ===')
CARDS={c['id'] for c in yaml.safe_load(open('spec/metric-cards.yml'))['metric_cards']}
OUTL={f"{s['id']}/{a['id']}":a for s in OUT['series'] for a in s['articles']}
specfail=0
for f in sorted(glob.glob('spec/pages/*/*.yml')):
    rel=os.path.relpath(f,'spec/pages')[:-4]
    d=yaml.safe_load(open(f))
    for cond,msg in [(d['id']!=os.path.basename(rel),'id 与路径不符'),
                     (d['series']!=rel.split('/')[0],'series 与路径不符'),
                     (rel not in OUTL,'不在 OUTLINE.yml 里')]:
        if cond: print(f'  ✗ {rel}: {msg}'); specfail+=1
    if rel in OUTL:
        a=OUTL[rel]
        for k in ('title','value'):
            if d.get(k)!=a.get(k): print(f'  ✗ {rel}: {k} 与 OUTLINE 不一致'); specfail+=1
        # sections 是 OUTLINE 的镜像：条数、标题、内容都得一样
        ds=d.get('sections') or []; os_=a.get('sections') or []
        if len(ds)!=len(os_):
            print(f'  ✗ {rel}: sections 条数 {len(ds)} 与 OUTLINE {len(os_)} 不一致'); specfail+=1
        else:
            for i,(x,y) in enumerate(zip(ds,os_)):
                if x.get('title')!=y.get('title'):
                    print(f'  ✗ {rel}: sections[{i}] 标题与 OUTLINE 不一致'); specfail+=1
                elif x.get('content')!=y.get('content'):
                    print(f'  ✗ {rel}: sections[{i}]「{y.get("title")}」内容与 OUTLINE 不一致'); specfail+=1
    for c in d.get('data_cards') or []:
        if c not in CARDS: print(f'  ✗ {rel}: 未知口径卡 {c}'); specfail+=1
for c in yaml.safe_load(open('spec/metric-cards.yml'))['metric_cards']:
    for u in (c.get('used_in') or [])+[ (c.get('chart') or {}).get('page') ]:
        if u and not os.path.exists(os.path.join('spec/pages',u+'.yml')):
            print(f'  ✗ 口径卡 {c["id"]}: 引用的页没有 spec 文件 {u}'); specfail+=1
print(f'  {len(glob.glob("spec/pages/*/*.yml"))} 个 spec 页 · {len(CARDS)} 张口径卡 · 交叉引用 {"✓" if not specfail else "✗"}')
fail+=specfail

# ── 正文里的小标题要跟 OUTLINE 的 section 标题对得上 ────────────
print('\n=== 正文标题 / OUTLINE section 标题 ===')
headbad=0
for s in OUT['series']:
    for a in s['articles']:
        doc=f"docs/{s['id']}/{a['id']}/cn.md"
        if not os.path.exists(doc): continue
        txt=open(doc,encoding='utf-8').read()
        heads=set(re.findall(r'^## (.+)$', txt, re.M))
        for sec in a.get('sections') or []:
            t=sec.get('title')
            # 「站内哪几篇讲过」是元信息段，不是正文小标题
            if t=='站内哪几篇讲过': continue
            if t in heads: continue
            # 允许正文给标题加前缀（「第 1 步 · 把问题说清楚」）
            if any(h.endswith('· '+t) for h in heads): continue
            # 允许正文用加粗小标题代替 ## （**标题** 或 **标题。** 起头的行内小标题）
            if re.search(r'^\*\*'+re.escape(t)+r'[。.]?\*\*', txt, re.M): continue
            print(f'  ✗ {s["id"]}/{a["id"]}: 正文里没有小标题「{t}」'); headbad+=1
print(f'  正文标题 {"✓" if not headbad else "✗"}')
fail+=headbad

# ── 「站内哪几篇讲过」指到的页必须是真的（OUTLINE 与 spec 页都要查）──
print('\n=== 站内互引 ===')
IDOF={f"{s['id']}/{a['id']}":a for s in OUT['series'] for a in s['articles']}
xrefbad=0
def check_xref(where, secs):
    global xrefbad
    for sec in secs or []:
        if sec.get('title')!='站内哪几篇讲过': continue
        for ref in re.split(r'[、,，]', sec.get('content') or ''):
            ref=ref.strip()
            if not ref: continue
            if ref in IDOF: continue
            # 也接受裸的篇名（同一 series 内）
            same=[k for k in IDOF if k.split('/')[1]==ref]
            if len(same)==1: continue
            print(f'  ✗ {where}: 站内互引指向不存在的页 {ref}')
            xrefbad+=1
for s in OUT['series']:
    for a in s['articles']:
        check_xref(f"{s['id']}/{a['id']}", a.get('sections'))
for f in sorted(glob.glob('spec/pages/*/*.yml')):
    rel=os.path.relpath(f,'spec/pages')[:-4]
    check_xref(f'spec {rel}', (yaml.safe_load(open(f)) or {}).get('sections'))
print(f'  站内互引 {"✓" if not xrefbad else "✗"}')
fail+=xrefbad

print('\n--- 硬伤数:',fail,'---')
