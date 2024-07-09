# GitHub Glossary
## Git vs. Github
**Git** is a version control system (VCS) that allows you to manage and keep track of your source code history. **Github** is an online (cloud-based) repository hosting platform that uses git. 

	Github to git is like Steam to PC games

## git vs. gh
In terminal, you’ll see some commands start with ‘git’ and other start with ‘gh’

git: the VCS– you don’t have to use github. You can use BitBucket, Gitlab, etc. 

gh: specifically for github

### Staging

Github uses staging, which means marking changes in the working directory to be included in your next commit. Basically, before saving your progress, you can choose what changes you want to include. 



## Terminal Commands for Github

### Setting up & Initalizing
| command    | use |
| -------- | ------- |
| git config --global user.name "[firstname lastname]" | Sets up a name that can be identifible    |
| git config --global user.email "[email]" | sets up the email address/account that is associated with changes     |
| git init    | initalize an existing directory as Git Repository    |
| git clone [url] <br> gh repo clone [Organization/Repository] | clone the repository from cloud to your local host. Changes locally will hav to be pushed to cloud to update the repo |



### Updating and Sharing
Before I get into syntax, let's address definitons: 

**add**: Stages a change for the next commit. You're basically marking the files as ready. 

**commit**: Saves the staged changes to your LOCAL repository. It creates a snapshot of the file in it's current statement

**push**: Sends your local committed changes to the remote repository.


| command    | use |
| -------- | ------- |
| git remote add [alias] [url]| add a git url as an alias. The alias is usually 'origin'    |
| git fetch [alias] |fetch down all the branches from the git remote. Retreive updates from a remote repo but doesn't merge them into your current working branch. You can review changes before integrating them     |
| git merge [alias]/[branch] | combines changes from one branch to another branch |
| git pull | takes all commits from a remote repository and integrates them into yur current branch | 
| git push [alias][branch] | sends local branch commits to remote repository branch | 
| git commit -m "[message]" | commits your current content as a new commit with a message to add context |


To simplify it, git pull is a combo of fetch+merge.

### Branches

Github uses *branches* to create seperate lines of development in a repository. It keeps it clean, organized, and allows for fixing bugs or adding features. Multiple developers can work on 1 project simultaneously without messing with each other's work. 

| command    | use |
| -------- | ------- |
| git branch -a | see all the branches (local & remote). The branch you are on is marked with a *    |
|git branch [branch-name] | create a new branch at the current commit |
|git checkout [branch-name] | switch to another branch |
|git merge [branch] | merge the branch into your current one | 
| git log | show all commits in your current branch's history |
