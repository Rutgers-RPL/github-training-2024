# GitHub Glossary
## Git vs. Github
**Git** is a version control system (VCS) that allows you to manage and keep track of your source code history. **Github** is an online (cloud-based) repository hosting platform that uses git. 

	Github to git is like Steam to PC games

## git vs. gh
In terminal, you’ll see some commands start with ‘git’ and other start with ‘gh’

git: the VCS– you don’t have to use github. You can use BitBucket, Gitlab, etc. 

gh: specifically for github

### Staging

Git uses staging, which means marking changes in the working directory to be included in your next commit. Basically, before saving your progress, you can choose what changes you want to include. 

Let's use an analogy to simplify this. Let's say we have a group project and everyone has their own notebooks with their own research. To make it easier, we decide to make a shared binder where everyone can share their notes. 

*Staging Area*: Temporary placeholder for your files that you plan to add and review. Think of it as a folder within your binder where you temporarily place the papers (files) you're ready to add to your project. This folder helps you organize and review what will be added to the binder.

The shared binder is called a **REMOTE REPOSITORY.** It allows users to add their code in from their local computers to the shared repository on cloud.


## Terminal Commands for Github

### Setting up & Initalizing
| command    | use | 
| ------- | ------- |
| git config --global user.name "[firstname lastname]" | Sets up the name that you use whenever you commit a change to a repository. If you save your changes, it will be under the name you put in so when people refer they can see its YOUR changes.    |
| git config --global user.email "[email]" | sets up the email address/account that is associated with your changes in the repository    |
| git init    | initalize an existing directory as Git Repository    |
| git clone [url] <br> gh repo clone [Organization/Repository] | clone the repository from cloud to your local host. Changes locally will have to be pushed to cloud to update the repo |



### Updating and Sharing
Before I get into syntax, let's address definitons. We talked about staging areas being a tempoary holder: 

**add**: You add the changed files into your staging area.  

**commit**: Saves the staged changes to your LOCAL repository. It creates a *snapshot* of the repository in it's current statement

**push**: Sends your local committed changes to the remote repository. The staging area is now empty.


| command    | use |
| -------- | ------- |
| git remote add [alias] [url]| This command lets you connect your personal code to the shared repository. The 'git remote add' part tells Git you want to add a new connection to the remote repository with the nickname '[alias]'. The URL is the location of the shared repository. |
| git fetch [alias] |Let's say your friend updated the repo and you want to review the changes before putting them in your code. You use 'git fetch' to get the latest updates from the remote repo and the '[alias]' is the same nickname from when you added the repository in the previous command. However, git fetch DOES NOT add the changes to your code automatically.     |
| git merge [alias]/[branch] | Let's say you reviewed their code and you're ready to integrate that code to your code. Git merge does just that-- it adds the changes to your code.  |
| git pull | This basically does the work of git fetch and git merge in one command. It's when you know fosho that your friends code is good and you want to add it to your repository. | 
|git add [filename] | This command adds the specific changed file you're referencing to in [filename] to the staging area. You're adding your new notes/changes into the tempoary section of the binder. |
|git add . | This commands all the files that you changed to the staging area. The '.' is what makes it ALL the files you've changed | 
| git push [alias][branch] | Now you've coded a function and you want to add that to the online repo. You use git push to add your code. Sometimes, you have to make a PR (pull request).  | 
| git commit -m "[message]" | commits your current content as a new commit with a message to add context. Whenever you commmit, it's a good idea to add a message for context to explain what you're commiting |
|git head| Similar to a bookmark telling you which note you're on, git head tells you which commit you're working on. |

The head is referred to as the current commit you are working on. 



**PULL REQUEST (PR)**: Based on the permissions of your repository, you can't always just immediately add your code. A pull request is when you push your changes to a different branch and you open a 'pull request' on the github website so someone can review your code before it's added into the repository. It's a good way of checking each other and not just messing up the code.

### History & Branches

Github uses *branches* to create seperate lines of development in a repository. Let's say we want each team to work on seperate parts of the project without interfering with each other's work. We create separate sections for each member's contributions. It keeps it clean, organized, and allows for fixing bugs or adding features.
	The *Main* branch is the branch with all the finalized code and details

| command    | use |
| -------- | ------- |
| git branch -a | see all the branches (local & remote). The branch you are currently working is marked with a *    |
|git branch [branch-name] | create a new branch at the current commit. Basicaly, it's like adding a new section at the same place you're working on. It does not change the current section |
|git checkout [branch-name] | switch to another branch.  |
|git merge [branch] | merge the branch into your current one.You're combining two sections of the binder to get one section of combined code/info. You would usually find yourself merging your own branch into the main branch. | 
| git log | This show all commits in your current branch's history |
|git status | Shows the current state of your project, listing changes that are staged, unstaged, and untracked. This helps you see where your files currently area.| 
|git rm [filename]| Deletes a file from both your project repository (binder) and your local workspace (desk), helping you keep your project tidy and up-to-date.|


### Conflicts

A Merge conflict is an issue that occurs when changes in different branches cannot be automatically merged. It's like having two team members who made different changes to the same section of the binder, requiring discussion to decide which version to keep.


