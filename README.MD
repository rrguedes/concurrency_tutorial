# Introduction

This is a simple code snippet on how to understand and implement concurrency in Python using the asyncio module.
I hope this example could be used as a refresher for developers like me who don't get into concurrency stories very often.

Please check the async.py comments to be guided through the concepts and behaviors expected to be implemented when creating concurrent systems.

This is not an exaustive guide and additions may be included for clarity or to detail concepts.

Thanks
Rafael
Follow me on X: @investeamapa

# Time

Time is the most important resource in software engineering. The idea behind concurrent is that you need to save time.

Imagine that you're preparing your breakfast before get to work. You usually prepare coffee, a toast and some scrambled eggs.
Ask yourself, what is more efficient? Preparing and getting the coffee ready first, then start the toast and then the eggs. Hell no! No one wants old coffee. Also, your boss will probably not like you arriving late because your breakfast took a couple hours to be prepared.

What to do, instead?

Why don't you start the coffee, let the machine do the work, then setup the toaster letting it work, while you prepare the eggs? More efficient, hum!?

That's the idea.

You're hopefully hungry (for knowledge) by know! Go check the code examples, run the sync and async versions and check out the results.