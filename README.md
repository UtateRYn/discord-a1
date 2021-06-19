<h2>
what did i do
</h2>
<p>
In this project, I aimed to display users who joined and left the Discord channel on a text channel of your choice.
</p>

<h2>
How to use
</h2>
<p>
it is very easy to use, all you have to do is customize the following parts according to you
</p>

<p>
but before that you need to add the library to your project
</p>

```python
pip install discord.py
```


> 1) In this section, you enter the name of the channel you want your bot to greet the logged in users in the part that says 'the name of your reception room'.

```python
channel = discord.utils.get(member.guild.text_channels, name="the name of your reception room"
```
> 2) The part you need to change in the following part is 'your token' here you need to enter the token of your Discord bot

```python
Bot.run("your token")
```

<p>
I drink a lot of coffee while developing projects if you want to buy me a coffee 
<a href="https://www.patreon.com/pressl">Patreon</a>
</p>
