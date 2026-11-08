#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""组装一页 cn.md：正文模板 + 用 tools/chart.py 生成的图块。

用法：
    python3 tools/build_page.py <模板.md.in> <输出.md>

模板里写 {{chart:JSON_SPEC|alt_name}} 占位，脚本会展开成
「裸 URL 块 + 可点的图」那一段。占位可以重复用同一张图。
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chart import build, block

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def expand(m):
    spec = json.loads(m.group(1))
    alt = m.group(2)
    return block(build(spec), alt)


def main():
    tpl_path, out_path = sys.argv[1], sys.argv[2]
    tpl = open(tpl_path, encoding='utf-8').read()
    body = re.sub(r'\{\{chart:(.+?)\|([^}]+)\}\}', expand, tpl, flags=re.S)
    open(out_path, 'w', encoding='utf-8').write(body)
    print(f'{out_path}  {len(body)} 字符')


if __name__ == '__main__':
    main()
