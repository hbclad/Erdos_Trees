# Erdos_Trees
Erdos group project involving trees?

GITHUB

After talking to a more git proficient friend this is gonna be my 'workflow' as they call it:
- git pull origin main 
-git branch name_of_branch
-git checkout name_of_branch 
-git push origin name_of_branch

Then do my edits, add files, etc. in vscode.  Making sure that I'm in the branch.  
When I am done:

-git add files_changed
-git commit -m "commit message"

-git push origin name_of_branch

Now the branch on the remote repo should have the updates shown, and it should prompt you to create a pull request.  Create the pull request and then we can merge it.  

-Then you can delete the branch on the remote repo
-Then you can locally delete the branch using: git branch -d name_of_branch
(You cannot delete the branch if you are still in it.  Use git branch main to go to the main branch)
