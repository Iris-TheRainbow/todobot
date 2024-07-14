# TODO Bot
A very simple TODO Discord bot created with the intent of helping the @unofficial-rev-port team
##Commands
The bot's keyword is `todo`. All commands must start with this.
You access your own todo by default. If you want to access a shared todo, add that next after `todo`. For example, `todo rhi` would access the shared todo `rhi`. You can open a new shared todo with `todo new <name>`.
To manipulate your todo, you can use the commands `add` to add a new item to the list. It has an optional position componet at the end that puts the new item in a specific spot (ie. `todo add Fix LibREVHub 1` puts it in the first slot of your todo list). `todo move <initial> <final>` can move an item. `todo rename <position> <name>` will rename an item on your list. `todo remove <position>` will remove the item in the given position.
Remember, inserting the name of the shared todo between the keyword and command will manipulate that todo, like `todo hwc add Make node-can-bridge work 1` will add 'Make node-can-bridge work' to the first slot of the 'hwc' list.
