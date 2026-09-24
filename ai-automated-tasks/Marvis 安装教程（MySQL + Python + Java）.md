# Marvis 安装教程 v3（MySQL + Python + Java）终稿

> 整理自「Marvis 帮小白装 MySQL」「Marvis 帮小白装 Python」「Marvis 一键安装 Java」三套图文教程，已将教程内图文画面全部转写为纯文本内容，并修正跨平台、检查步骤、环境变量等逻辑问题。
> 用途：把「用 Marvis（马维斯）帮小白安装开发环境」的提示词创作思路与成品提示词合并成一份可直接复用的纯文本文档。
> 适用系统：Windows / macOS / Linux，具体命令已按系统区分。

---

## 目录

- [一、马维斯帮小白装 MySQL](#一马维斯帮小白装-mysql)
- [二、马维斯帮小白装 Python](#二马维斯帮小白装-python)
- [三、马维斯一键安装 Java](#三马维斯一键安装-java)
- [四、提示词模板速查（可直接复制）](#四提示词模板速查可直接复制)
- [五、通用方法论：安装三步法](#五通用方法论安装三步法)

---

## 一、马维斯帮小白装 MySQL

### 1.1 教程封面

封面标题：**马维斯帮小白装 MySQL**

### 1.2 提示词创作思路：安装 / 配置 / 检查

安装工作拆分为三步，让 Marvis 有章法地干活：

| 步骤 | 要做什么 |
|---|---|
| **安装** | 前往 MySQL 官方网站，下载对应系统版本的安装包；安装过程中设置自定义数据库账户与登录密码 |
| **配置** | 安装完成后，手动将 MySQL 的 `bin` 目录配置到系统环境变量 `PATH` 中；并确保 MySQL 服务已启动 |
| **检查** | 打开终端 / 命令行，执行连接命令校验安装是否成功：`mysql -u [账户] -p`，回车后输入密码 |

### 1.3 安装 MySQL 提示词（成品，可直接复制）

```text
下载安装 MySQL Community Server [版本号]，安装过程中设置数据库账户：[自设用户名]、登录密码：[自设密码]；
安装完成后将 MySQL 的 bin 目录加入系统环境变量 PATH，并启动 MySQL 服务。
安装完成后，请执行 mysql -u [自设用户名] -p 验证连接。
```

**参数说明：**

- `[版本号]`：留空时，Marvis 将默认安装最新版本。
- `[自设用户名]` / `[自设密码]`：按自己习惯命名，密码务必自行保管。
- 检查命令 `mysql -u [账户] -p` 回车后输入密码，避免密码明文保存在命令历史记录中。

### 1.4 各系统补充说明

**Windows：**

- 安装时勾选“Add MySQL to PATH”或安装后手动将 `C:\Program Files\MySQL\MySQL Server X.X\bin` 加入系统 `PATH`。
- 启动服务：打开“服务”管理器，找到 `MySQL` 服务，右键启动；或使用 `net start mysql`。

**macOS：**

- 使用 Homebrew 安装：`brew install mysql`，然后 `brew services start mysql`。
- 将 `/usr/local/mysql/bin` 或 Homebrew 路径加入 `~/.zshrc` 或 `~/.bash_profile` 的 `PATH`。

**Linux：**

- 使用包管理器安装，例如 `sudo apt install mysql-server`。
- 启动服务：`sudo systemctl start mysql`（部分发行版服务名为 `mysqld`），并设置开机自启 `sudo systemctl enable mysql`；`enable` 仅配置开机自动运行，不会启动当前服务。
- 将 `/usr/bin` 或 MySQL 安装目录下的 `bin` 加入 `PATH`。
- 补充：Ubuntu 安装完成后，MySQL 默认使用 `auth_socket` 认证，root 用户需要通过 `sudo mysql` 登录，再手动设置数据库密码。

---

## 二、马维斯帮小白装 Python

### 2.1 教程封面

封面标题：**马维斯帮小白装 Python**

### 2.2 提示词创作思路：安装 / 配置 / 检查

Python 与 MySQL 同样是「安装 → 配置 → 检查」三步走。

**① 安装**
前往 Python 官网，或阿里、清华镜像站下载对应安装包。
> 注意：请不要在 Marvis 软件内部安装 Python，因为 Marvis 内部可能自带隔离沙箱环境，直接在内部安装 Python 容易引发路径冲突。

**② 配置**
将 Python 安装路径添加至系统环境变量 `PATH`。
- Windows：右键「此电脑」→ 属性 → 高级系统设置 → 环境变量，将 Python 安装目录及其 `Scripts` 目录加入 `Path`。
- macOS / Linux：在 `~/.zshrc`、`~/.bashrc` 或 `~/.bash_profile` 中添加 `export PATH="[Python安装目录]/bin:$PATH"`，然后执行 `source 配置文件名` 重载 Shell，使环境变量配置生效。示例：`source ~/.zshrc`。

**③ 检查**
安装好后在命令行界面输入 `python --version` 或 `python3 --version` 查看版本，再输入 `python` 或 `python3` 进入交互模式，看到 `>>>` 提示符即说明安装成功。
> 进阶校验：安装验证完成后，建议重启命令行窗口，输入 `pip show pip` 查看 pip 完整信息。

### 2.3 安装 Python 提示词（成品，可直接复制）

```text
请不要在 Marvis 软件内部安装 Python，从 [下载地址] 下载、安装 [版本号] 版本的 Python，
安装至 [存放位置]，并协助我完成环境变量配置。
安装完成后，请执行 python --version 或 python3 --version 验证安装。
```

**需修改的参数：**

| 参数 | 说明 |
|---|---|
| `[下载地址]` | 官方网址（慢），建议阿里、华为或清华镜像 |
| `[版本号]` | 你需要的 Python 版本，默认 Marvis 自定 |
| `[存放位置]` | 默认系统盘 C 盘，可以自定 |

**各系统补充：**

- Windows：勾选“Add Python to PATH”，或手动添加安装目录和 `Scripts` 目录。
- macOS / Linux：使用 `python3` 命令，pip 使用 `pip3`；配置写入 shell 配置文件。

---

## 三、马维斯一键安装 Java

### 3.1 教程封面

海报标题：**Marvis 一键安装 Java**
标签：安装 Java 提示词
海报署名：WorkBuddy

### 3.2 提示词创作思路：安装 / 配置 / 检查

Java 同样适用三步法：

**① 安装**
通过官网或镜像下载 JDK 安装包，按目标系统选择 Windows / macOS / Linux 版本，安装至指定目录。

**② 配置**
- Windows：新建系统变量 `JAVA_HOME=[安装目录]`，编辑 `Path` 变量，新增 `%JAVA_HOME%\bin`。
- macOS / Linux：在 `~/.zshrc`、`~/.bashrc` 或 `~/.bash_profile` 中添加：
  ```bash
  export JAVA_HOME=[安装目录]
  export PATH="$JAVA_HOME/bin:$PATH"
  ```
  然后执行 `source 配置文件名` 使配置生效。

**③ 检查**
命令行执行 `java -version` 和 `javac -version`，能正确输出版本号即安装成功。

### 3.3 安装 Java 提示词（成品，可直接复制）

**Windows 版：**

```text
自动安装 Java JDK [版本号]：通过 [下载地址] 下载 Windows 安装包，安装至 [安装目录]；
配置环境变量 JAVA_HOME=[安装目录]，将 %JAVA_HOME%\bin 添加进 PATH。
安装完成后，请执行 java -version 和 javac -version 验证安装。
```

**macOS / Linux 版：**

```text
自动安装 Java JDK [版本号]：通过 [下载地址] 下载 [对应系统] 安装包，安装至 [安装目录]；
配置环境变量 JAVA_HOME=[安装目录]，将 $JAVA_HOME/bin 添加进 PATH。
安装完成后，请执行 java -version 和 javac -version 验证安装。
```

**参数说明：**

| 参数 | 说明 |
|---|---|
| `[版本号]` | 留空时，Marvis 将默认安装 Java 最新稳定版本 |
| `[下载地址]` | Java JDK 安装包下载地址（官网 / 镜像） |
| `[对应系统]` | 按目标系统选择安装包（Windows / macOS / Linux） |
| `[安装目录]` | JDK 安装路径，同时用作 `JAVA_HOME` 的值 |

**要点：**

- Windows 环境变量固定写法：`JAVA_HOME=[安装目录]`，并把 `%JAVA_HOME%\bin` 追加进 `PATH`。
- macOS / Linux 环境变量写法：`JAVA_HOME=[安装目录]`，并把 `$JAVA_HOME/bin` 加入 `PATH`。

---

## 四、提示词模板速查（可直接复制）

**装 MySQL：**

```text
下载安装 MySQL Community Server [版本号]，安装过程中设置数据库账户：[自设用户名]、登录密码：[自设密码]；
安装完成后将 MySQL 的 bin 目录加入系统环境变量 PATH，并启动 MySQL 服务。
安装完成后，请执行 mysql -u [自设用户名] -p 验证连接。
```

**装 Python：**

```text
请不要在 Marvis 软件内部安装 Python，从 [下载地址] 下载、安装 [版本号] 版本的 Python，
安装至 [存放位置]，并协助我完成环境变量配置。
安装完成后，请执行 python --version 或 python3 --version 验证安装。
```

**装 Java（Windows）：**

```text
自动安装 Java JDK [版本号]：通过 [下载地址] 下载 Windows 安装包，安装至 [安装目录]；
配置环境变量 JAVA_HOME=[安装目录]，将 %JAVA_HOME%\bin 添加进 PATH。
安装完成后，请执行 java -version 和 javac -version 验证安装。
```

**装 Java（macOS / Linux）：**

```text
自动安装 Java JDK [版本号]：通过 [下载地址] 下载 [对应系统] 安装包，安装至 [安装目录]；
配置环境变量 JAVA_HOME=[安装目录]，将 $JAVA_HOME/bin 添加进 PATH。
安装完成后，请执行 java -version 和 javac -version 验证安装。
```

---

## 五、通用方法论：安装三步法

不管装 MySQL、Python 还是 Java，统一套用：

1. **安装**：官网或镜像站下载对应操作系统版本的安装包。
2. **配置**：
   - MySQL：安装过程中设账户密码；安装后将 `bin` 目录加入 `PATH`；启动 MySQL 服务。
   - Python：将安装目录及 `Scripts`（Windows）或 `bin`（macOS / Linux）加入环境变量。
   - Java：新建 `JAVA_HOME`，将 `bin` 加入 `PATH`（Windows 用 `%JAVA_HOME%\bin`，macOS / Linux 用 `$JAVA_HOME/bin`）。
3. **检查**：命令行验证。
   - MySQL：`mysql -u [账户] -p`，回车后输入密码。
   - Python：`python --version` 或 `python3 --version`，再输入 `python` 或 `python3` 看到 `>>>` 即成功。
   - Java：`java -version` / `javac -version`。

> 提示：以上“检查”步骤已写入各提示词模板，复制给 Marvis 后会一并执行。若 Marvis 未执行校验步骤，请手动打开终端完成验证。
