We will be ingesting, transforming, storing, transforming, and displaying some data.

### 1. First, we'll need data

ImageNet (http://imagenet.stanford.edu/) is a commonly used dataset in machine learning research. We'll be using its taxonomy system.

When you go to http://imagenet.stanford.edu/synset?wnid=n02486410, you'll see a tree on the left. Your job is to get this tree and transform it into a linear form, like this:

```
[
    {name: 'ImageNet 2011 Fall Release', size: 32326},
    {name: 'ImageNet 2011 Fall Release > plant, flora, plant life', size: 4486},
    {name: 'ImageNet 2011 Fall Release > plant, flora, plant life > phytoplankton', size: 2},
    {name: 'ImageNet 2011 Fall Release > plant, flora, plant life > phytoplankton > planktonic algae', size: 0},
    {name: 'ImageNet 2011 Fall Release > plant, flora, plant life > phytoplankton > diatom', size: 0},
    ...
    {name: 'ImageNet 2011 Fall Release > plant, flora, plant life > microflora', size: 0},
]
```

We'll use `>` as a separator of categories/subcategories.

It's completely up to you how you download this data, everything is allowed.

### 2. Second, we'll need to store it somewhere

Create a database (use any database system you like or want to try) to store these tuples `(string, number)` and fill it with the data you obtained in the first step.

### 3. Making sense of it

Next, we'll convert it back to a tree. Like this:

```
{
    name: 'ImageNet 2011 Fall Release',
    size: 32326,
    children: [
        {
            name: 'plant, flora, plant life',
            size: 4486,
            children: [
                {
                    name: 'phytoplankton',
                    size: 2,
                    children: [
                        ...
                    ]
                },
                ...
            ]
        },
        ...
    ]
}
```

* Can you write an algorithm that will output such a tree? No cheating here, you have to read this data in a linear form from the database.
* What is the complexity of your algorithm (in big O notation)?

### 3. Now it's time to show the data again

* Can you design and build an interface to show this data?
* Can you implement search in this UI?

<hr>

Feel free to use any tools, frameworks or libraries. Whatever you are most comfortable with or something new that you wanted to try for a long time. Just let me know what you chose, why, and what was your previous experience with it.

