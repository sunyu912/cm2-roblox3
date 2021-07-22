# How to update the curriculum repo

contact: [@ArielJiang0520](https://github.com/ArielJiang0520)

## Menu


- [Lv 1](#lv1) (Github :x:Markdown :x:Curriculum Repo:x:)
- [Lv 2](#lv2) (Github :heavy_check_mark:Markdown :x:Curriculum Repo:x:)
- [Lv 3](#lv3) (Github :heavy_check_mark:Markdown :heavy_check_mark:Curriculum Repo:x:)
- [Lv 4](#lv4)  (Github :heavy_check_mark:Markdown :heavy_check_mark:Curriculum Repo:heavy_check_mark:)
- [Common Q&A](#qa)
- [Image Linking](#image)

## LV1 <a name='lv1'></a>

As a curriculum developer, the two things you need to familiarize yourself with are "push" and "pull". I used this [video]() to learn, you can find whatever resource is convenient for you.

After you've learned the basics of Github, continue to **LV 2**

## LV2 <a name='lv2'></a>

The basics of Markdown syntax can be found in this [cheatsheet](https://www.markdownguide.org/basic-syntax/).

For the purpose of this repo, you will need to specifically know these two things:

- [how to properly link images](#image)
- [how to write code blocks](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks)

By the way, here is a [video](https://youtu.be/ieHsriFbkRs) I made awhile ago explaining this whole process. It's around 5 minute, so if you want, you can take a look at it

## LV3 <a name='lv3'></a>

There are some naming conventions you need to follow. The `naming conventions.md` file is in every repo. If you don't follow them, it might cause push failure.

One more thing, because this is really important: we are using [this method](#image) to link images, it's not the usual way!

## LV4 <a name='lv4'></a>

You are good to go! Remember to always push to the `master` branch, not creating your own branch.

## Q&A

- Q: What if I encounter a push failure?
- A: Check your naming for the folders. Otherwise contact me on basecamp. Always report the push action failure.



- Q: What if my changes are not showing on the website?
- A: Give it a few minutes. Check if there's a push failure and contact me.



- Q: What if I see a typo or a bug in the repo, should I fix it myself?
- A: Yes, you should fix it, but also write a clear commit message on what you did.

## Image Linking <a name='image'></a>

Markdown files are just plain text files, when you embed images, the markdown files do not "own" those images, but just keep a weak reference to external image files. When you move those images or delete them, the pictures showing on markdown files will also be invalid. This brings up the maintenance cost.

While we are trying to figure out a solution, we are keeping all of our images in the google doc that is shared between Coding Minds employees. For example, all Roblox 1's images are saved in the Roblox 1 Master Reference document. 

I assume you have the access to the folder of whichever course you are working on. If you do not, please contact me.

Otherwise, please first insert your local image in the Google doc and copy the link to your markdown file.



Last update: 12/14/2020