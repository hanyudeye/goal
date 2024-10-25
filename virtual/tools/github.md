## github 仓库按照star 降序排列

https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md

## git clone --depth=1 后，怎么把所有分支都clone下来

`git clone --depth=1` 只会克隆指定仓库的最新提交，并且默认只克隆当前的默认分支，这样可以节省空间和时间。如果在克隆之后你需要克隆该仓库的所有分支，并且继续保持浅克隆（即保留最新的历史），可以按照以下步骤操作：

### 1. **使用 `--no-single-branch` 参数**
   `--no-single-branch` 参数可以与 `--depth=1` 一起使用，来克隆所有分支的浅历史记录。

   ```bash
   git clone --depth=1 --no-single-branch <repository-url>
   ```

   这样会克隆所有分支，但每个分支仍然只包含最新的提交历史。

### 2. **克隆后下载所有分支**
   如果已经使用 `git clone --depth=1` 克隆了仓库的默认分支，并想在此基础上获取其他分支，可以通过以下步骤完成：

   #### a. **获取所有分支的引用**
   执行以下命令来下载所有分支的引用：
   ```bash
   git fetch --depth=1 origin '+refs/heads/*:refs/remotes/origin/*'
   ```

   这个命令会以浅克隆的方式抓取所有的分支，并在本地创建相应的远程分支引用。

   #### b. **查看所有分支**
   获取所有分支后，你可以用以下命令查看所有的远程分支：
   ```bash
   git branch -r
   ```

   #### c. **检出其他分支**
   使用 `git checkout` 命令切换到想要的分支：
   ```bash
   git checkout <branch-name>
   ```

### 3. **将浅克隆转换为完整克隆（可选）**
   如果你决定不再需要浅克隆，可以使用以下命令将仓库的历史记录拉取完整：
   ```bash
   git fetch --unshallow
   ```

   这会把之前的浅克隆转换成完整的仓库克隆，包括所有历史记录。

### 总结
如果你想在克隆时获取所有分支并保留浅克隆，可以使用 `git clone --depth=1 --no-single-branch`；如果已经克隆了单个分支，则可以通过 `git fetch --depth=1` 来获取其他分支的浅克隆记录。


## fork 别人的仓库后只有一个分支，怎么办

当你从别人的仓库 **Fork** 过来后，只看到一个分支，而没有其他分支的情况，可能是因为 Fork 时默认只包含了默认分支（通常是 `master` 或 `main`）。你可以通过以下步骤来获取原仓库的其他分支。

### 1. **添加原始仓库为上游（upstream）**
   首先，确保你 Fork 的仓库的其他分支能够被追踪。你可以通过添加原始仓库（也就是你 Fork 的那个仓库）为一个远程仓库，称之为 **upstream**，然后从那里获取分支。

   1.1. **添加 upstream 远程仓库**
   使用以下命令，将原始仓库的 URL 作为上游（`upstream`）远程仓库添加：
   ```bash
   git remote add upstream <original-repo-url>
   ```
   例如：
   ```bash
   git remote add upstream https://github.com/original-owner/original-repo.git
   ```

   1.2. **验证远程仓库是否正确添加**
   运行以下命令查看远程仓库是否成功添加：
   ```bash
   git remote -v
   ```
   你应该看到 `origin`（指向你的 Fork 仓库）和 `upstream`（指向原始仓库）两行输出：
   ```
   origin    https://github.com/your-username/forked-repo.git (fetch)
   origin    https://github.com/your-username/forked-repo.git (push)
   upstream  https://github.com/original-owner/original-repo.git (fetch)
   upstream  https://github.com/original-owner/original-repo.git (push)
   ```

### 2. **获取原始仓库的所有分支**
   通过 `upstream` 远程仓库获取所有分支的引用：
   ```bash
   git fetch upstream
   ```

   这会将所有来自原始仓库（upstream）的分支信息同步到本地，但不会自动创建本地分支。

### 3. **查看并切换到其他分支**
   现在你可以使用以下命令查看所有上游分支（包括从 `upstream` 获取的）：
   ```bash
   git branch -r
   ```
   你会看到来自 `upstream` 的分支，例如：
   ```
   upstream/branch-1
   upstream/branch-2
   ```

   如果你想在本地使用其中的某个分支，使用以下命令检出并创建本地分支：
   ```bash
   git checkout -b <branch-name> upstream/<branch-name>
   ```
   例如：
   ```bash
   git checkout -b feature-branch upstream/feature-branch
   ```
   这样你就会在本地创建并切换到从 `upstream` 获取的 `feature-branch` 分支。

### 4. **将上游仓库的更改同步到本地**
   以后你可以定期从上游仓库同步更改，确保你 Fork 的仓库是最新的。使用以下命令获取上游的最新更改：
   ```bash
   git fetch upstream
   ```
   然后，可以将上游的更改合并到本地分支：
   ```bash
   git merge upstream/<branch-name>
   ```

### 总结
- 当你 Fork 了一个仓库并且只有一个分支时，通常是因为默认只包含了那个分支。你可以通过添加上游（原始仓库）为远程仓库，并从中拉取其他分支。
- 使用 `git remote add upstream` 来添加上游，`git fetch upstream` 来获取所有分支，并使用 `git checkout -b` 来创建并切换到其他分支。

这样你就可以访问原始仓库的所有分支并在本地进行开发。