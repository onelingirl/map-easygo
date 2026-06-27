# 请在本目录创建 .env 文件或设置环境变量：
# EASYGO_QQ=969913554
# EASYGO_PASS=abcd123456
#
# Windows PowerShell: $env:EASYGO_QQ="969913554"; $env:EASYGO_PASS="abcd123456"
# Windows CMD:        set EASYGO_QQ=969913554 && set EASYGO_PASS=abcd123456
# Linux/macOS:        export EASYGO_QQ=969913554 && export EASYGO_PASS=abcd123456

import os

qq_list = [
    [os.environ.get("EASYGO_QQ", "969913554"), os.environ.get("EASYGO_PASS", "abcd123456")]
]