# 林分调查与养护资料

本项目整理造林批次、分期样方调查、林分状态和养护作业信息，供森林质量复核和年度养护计划使用。

## 资料

`data/manifest.json` 描述合成演练资料及字段。调查记录保留样方和调查方法标识，栽植与养护记录分别标明实际业务期间。

字段含义及有效期约定见[资料口径](资料口径.md)。

## 本地检查

使用 Python 3.11 或更新版本，无需安装第三方依赖。

```sh
python3 -m unittest discover -s tests -v
python3 -m compileall -q tests
```
