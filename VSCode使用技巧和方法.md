- [VSCode连接虚拟机](#vscode连接虚拟机)
- [Vscode插件todo-tree基本配置](#vscode插件todo-tree基本配置)

# VSCode连接虚拟机
1. 安装插件——Remote Development插件
2. 打开SSH并配置
- ![配置地址](./images/打开SSH并配置.png)
- Host CentosNat (自定义名称)
  HostName 192.168.3.128 (IP地址)
  User root (用户名)
  PORT 22
  这里port是端口号，如果连接两台linux虚拟机的时候记得在配置文件里面都要写上port端口号 一般默认22端口可多开使用！！！
- ![远程连接](./images/远程连接.png)
- ![连接](./images/连接.png)
- ![登录](./images/登录.png)
- ![登录1](./images/登录1.png)
- ![登录2](./images/登录2.png)

# Vscode插件todo-tree基本配置
1. 找到配置地址
   - ![找到配置地址](./images/找到配置地址.png)
2. 常设配置
```json
{
    "remote.SSH.remotePlatform": {
        "alias": "linux",
        "CentosNat": "linux"
    },
    "editor.codeActionsOnSave": {},
    "notebook.codeActionsOnSave": {

    },

    // todo-tree-config
    "todo-tree.regex.regex": "(//|#|<!--|;|/\\*|^|^\\s*(-|\\d+.))\\s*($TAGS)",
    // 是否区分大小写
    "todo-tree.regex.regexCaseSensitive": false,
    //在资源管理器视图中显示树
    "todo-tree.tree.showInExplorer": true,
    "todo-tree.general.tags": [
        "bug",
        "HACK",
        "FIXME",
        "TODO",
        "DONE",
        "tag",
        "XXX",
        "[ ]",
        "[x]"
    ],
    "todo-tree.highlights.defaultHighlight": {
        "icon": "checklist",
        "type": "tag",
        "foreground": "white",
        "background": "Orange",
        "opacity": 50,
        "iconColour": "Orange",
        "rulerColour": "Orange"
    },
    "todo-tree.highlights.customHighlight": {
        "TODO": {
            "icon": "check",
            "gutterIcon": true,
            "type": "line"
        },
        "FIXME": {
            "foreground": "black",
            // "iconColour": "yellow",
            "gutterIcon": true,
            "background": "red",
            "icon": "beaker",
            "rulerColour": "red",
            "iconColour": "red",
            "opacity": 50
        },
        "tag": {
            "background": "Magenta",
            "icon": "pin",
            "rulerColour": "Magenta",
            "iconColour": "Magenta",
            "rulerLane": "full",
            "opacity": 50,
        },
        "done": {
            "background": "DarkTurquoise",
            "icon": "verified",
            "rulerColour": "DarkTurquoise",
            "iconColour": "DarkTurquoise",
            "opacity": 50,
        },
        "bug": {
            "background": "green",
            "icon": "bug",
            "rulerColour": "green",
            "iconColour": "green",
            "opacity": 50,
        }
    }

}
```