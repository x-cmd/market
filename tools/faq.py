#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从一份 Python 数据生成 faq.yml。

用法：
    python3 tools/faq.py <数据文件.py> <输出 faq.yml>

数据文件是一个 dict：
    {
      'id': 'x-market-8-analysis-toolbox-04-adstock-decay',
      'groups': [
        {'name_en': ..., 'name_cn': ...,
         'qa': [{'id': ..., 'q_en': ..., 'q_cn': ...,
                 'a_en': ..., 'a_cn': ..., 'confidence': 10}]},
      ],
      'reference': 'docs/8-analysis-toolbox/04-adstock-decay/cn.md',
    }

长文本用折行块（>）写，单行用普通标量。
"""
import sys
import textwrap


def wrap_cjk(s, width):
    """按显示宽度折行，中文按 2 个字符算。

    中文不断句（不断在词中间），只按标点切；英文按空格切。
    """
    out = []
    line = ''
    w = 0

    def flush():
        nonlocal line, w
        if line:
            out.append(line)
        line = ''
        w = 0

    # 先切成「不切断的片段」：中文标点后切开，英文按空格切
    toks = []
    buf = ''
    for ch in s:
        if ord(ch) > 0x2E7F:
            if buf and ch in '。，、；：！？）」』':
                toks.append(buf + ch)
                buf = ''
            else:
                buf += ch
        elif ch == ' ':
            if buf:
                toks.append(buf)
                buf = ''
            toks.append(' ')
        else:
            buf += ch
    if buf:
        toks.append(buf)

    for t in toks:
        cw = sum(2 if ord(c) > 0x2E7F else 1 for c in t)
        if w + cw > width and line.strip():
            flush()
        line += t
        w += cw
    flush()
    return [l.rstrip() for l in out]


def block(s, indent):
    """把一段文字写成 YAML 折行块，宽度固定，行首带 indent。"""
    pad = ' ' * indent
    text = ' '.join(s.split())
    if not text:
        return f'{pad}> ""\n'
    lines = wrap_cjk(text, 96 - indent - 2)
    return f'{pad}>\n' + ''.join(f'{pad}  {ln}\n' for ln in lines)


def scalar(s):
    """单行标量；含特殊字符就加引号。"""
    s = ' '.join(s.split())
    if any(c in s for c in ':#{}[],&*?|-<>=!%@`"\'') or s.strip() != s:
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return s


def main():
    ns = {}
    exec(open(sys.argv[1], encoding='utf-8').read(), ns)
    d = ns['DATA']
    out = [f"id: {d['id']}", '', 'data:']
    for g in d['groups']:
        out.append('  - name:')
        out.append(f"      en: {scalar(g['name_en'])}")
        out.append(f"      cn: {scalar(g['name_cn'])}")
        out.append('    qa:')
        for q in g['qa']:
            out.append(f"      - id: {q['id']}")
            out.append('        question:')
            out.append(f"          en: {scalar(q['q_en'])}")
            out.append(f"          cn: {scalar(q['q_cn'])}")
            out.append('        answer:')
            out.append('          en:')
            out.append(block(q['a_en'], 12).rstrip('\n'))
            out.append('          cn:')
            out.append(block(q['a_cn'], 12).rstrip('\n'))
            out.append(f"        confidence: {q.get('confidence', 9)}")
            out.append('        reference:')
            out.append(f"          - {d.get('reference', '')}")
    open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    n = sum(len(g['qa']) for g in d['groups'])
    print(f"{sys.argv[2]}  {n} 条 QA（{len(d['groups'])} 组）")


if __name__ == '__main__':
    main()
