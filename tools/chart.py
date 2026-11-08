#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""画图助手：把一份小规格变成一条 draw URL。

用法：
    python3 tools/chart.py '{"type":"bar","title":"...","x":["A","B"],"y":[1,2]}'
    python3 tools/chart.py --file spec.json

规格（type 为 bar/hbar/line/area/scatter 时）：
    title   图标题
    x       类别（bar/hbar/line/area）或散点的 x 值
    y       数值（bar/hbar/line/area）或散点的 y 值
    series  [{"name": "...", "data": [...]}]  多系列时用这个
    colors  ["#2563eb", ...]
    yname   y 轴名
    stack   1 堆叠
    legend  1 显示图例
    w h     画布宽高，默认 760x420

输出：一条 https://x-cmd.com/draw/echarts?d=... URL
"""
import json, sys, urllib.parse

PALETTE = ['#2563eb', '#dc2626', '#64748b', '#f59e0b', '#0891b2', '#8b5cf6', '#65a30d', '#db2777']
BASE = 'https://x-cmd.com/draw/echarts'


def build(spec):
    t = spec.get('type', 'bar')
    w, h = spec.get('w', 760), spec.get('h', 420)
    colors = spec.get('colors') or PALETTE
    opt = {'title': {'text': spec.get('title', '')}, 'color': colors}
    series = spec.get('series')
    if not series:
        if t == 'scatter':
            pts = spec.get('points') or [{'x': x, 'y': y, 'name': n} for x, y, n in
                                         zip(spec.get('x', []), spec.get('y', []), spec.get('names', []))]
            series = [{'type': 'scatter', 'symbolSize': 16,
                       'data': [{'value': [p['x'], p['y']], 'name': p.get('name', '')} for p in pts],
                       'label': {'show': True, 'position': 'top', 'formatter': '{b}', 'fontSize': 10}}]
            opt['xAxis'] = {'type': 'value', 'name': spec.get('xname', '')}
            opt['yAxis'] = {'type': 'value', 'name': spec.get('yname', '')}
            opt['grid'] = {'left': 80, 'right': 40, 'top': 60, 'bottom': 60}
            opt['tooltip'] = {'trigger': 'item', 'formatter': '{b}'}
        else:
            # draw 渲染器不支持 series type 'hbar'——会画出空图（只有轴和标签，没有柱子）。
            # 横条要用 type 'bar'，同时把类目放到 y 轴、数值放到 x 轴。
            st = 'bar' if t == 'hbar' else t
            series = [{'name': spec.get('series_name', ''), 'type': st, 'data': spec.get('y', []),
                       'label': {'show': spec.get('label', True),
                                 'position': 'right' if t == 'hbar' else 'top',
                                 'formatter': '{c}' + ('%' if spec.get('percent') else '')},
                       'stack': spec.get('stack')}]
            cat = spec.get('x', [])
            if t == 'hbar':
                opt['xAxis'] = {'type': 'value', 'name': spec.get('yname', ''),
                                'axisLabel': {'formatter': '{value}%'} if spec.get('percent') else {'formatter': '{value}'}}
                opt['yAxis'] = {'type': 'category', 'data': cat, 'axisLabel': {'interval': 0}}
                opt['grid'] = {'left': 90, 'right': 60, 'top': 60, 'bottom': 50}
            elif t == 'bar':
                opt['xAxis'] = {'type': 'category', 'data': cat, 'axisLabel': {'interval': 0}}
                opt['yAxis'] = {'type': 'value', 'name': spec.get('yname', '')}
                opt['grid'] = {'left': 90, 'right': 50, 'top': 60, 'bottom': 60}
            else:
                opt['xAxis'] = {'type': 'category', 'data': cat, 'axisLabel': {'interval': spec.get('interval', 0)}}
                opt['yAxis'] = {'type': 'value', 'name': spec.get('yname', '')}
                opt['grid'] = {'left': 80, 'right': 40, 'top': 60, 'bottom': 50}
            opt['tooltip'] = {'trigger': 'axis', 'axisPointer': {'type': 'shadow'}}
    else:
        for s in series:
            s.setdefault('type', t)
            if t in ('line', 'area'):
                s.setdefault('smooth', True)
                s.setdefault('connectNulls', True)
        if spec.get('stack'):
            for s in series:
                s['stack'] = 'total'
        cats = spec.get('x', [])
        opt['xAxis'] = {'type': 'category', 'data': cats, 'axisLabel': {'interval': spec.get('interval', 0)}}
        opt['yAxis'] = {'type': 'value', 'name': spec.get('yname', ''),
                        'axisLabel': {'formatter': '{value}%'} if spec.get('percent') else {'formatter': '{value}'}}
        opt['grid'] = {'left': 80, 'right': 40, 'top': 60 if not spec.get('legend') else 80, 'bottom': 60}
        opt['tooltip'] = {'trigger': 'axis'}
        if spec.get('legend'):
            opt['legend'] = {'data': [s.get('name', '') for s in series], 'top': 30}
    opt['series'] = series
    d = urllib.parse.quote(json.dumps(opt, ensure_ascii=False, separators=(',', ':')), safe='')
    return f'{BASE}?d={d}&w={w}&h={h}'


def block(url, alt, width=760):
    """页面里一段图：裸 URL 块 + 可点的图。"""
    ex = url.replace('/draw/echarts?', '/draw/explore/echarts?')
    return f'```text\n{url}\n```\n\n<a href="{ex}"><img src="{url}" width="{width}" alt="{alt}"></a>'


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == '--file':
        spec = json.load(open(a[1], encoding='utf-8'))
    else:
        spec = json.loads(a[0])
    print(build(spec))
