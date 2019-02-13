//This stuff is for connecting to discord and using discord.js
const discord = require ('discord.js');
const pollyBot = new discord.Client();

//This is logging into the discord server
pollyBot.login('NDcwMDQ4MzAxMDMxNjIwNjE5.DjQmgg.3gr6cMTCNfi5tsmzN6xptFq7e1c');


//This just makes the bot repeat any messaegs that are sent by someone other than itself
pollyBot.on('message', message => {

	if(message.author.bot){
		return;
	}

    //That number is a channel id which refers to a specific channel in the server
		pollyBot.channels.get("545079453714350103").send(message.content)

});

//Listener event for when someone joins the server
pollyBot.on('guildMemberAdd', member => {
	console.log('User ' + member.user.username + ' has joined the server') // Sends a message in console that somone joined the server

	//Adds a role when they join
	var role = member.guild.roles.find('name', 'User');
	member.addRole(role);
});

//When a message is deleted it logs the deleted message and says who deleted it
pollyBot.on('messageDelete', async (message) => {
  const logs = pollyBot.channels.get("545079453714350103");
  if (message.guild.me.hasPermission('MANAGE_CHANNELS') && !logs) {
    message.guild.createChannel('logs', 'text');
  }
  if (!message.guild.me.hasPermission('MANAGE_CHANNELS') && !logs) { 
    console.log('The logs channel does not exist and tried to create the channel but I am lacking permissions')
  }  
  let user = ""

  const entry = await message.guild.fetchAuditLogs({type: 'MESSAGE_DELETE'}).then(audit => audit.entries.first())
    if (entry.extra.channel.id === message.channel.id
      && (entry.target.id === message.author.id)
      && (entry.createdTimestamp > (Date.now() - 5000))
      && (entry.extra.count >= 1)) {
    user = entry.executor.username
  } else { 
    user = entry.executor.username
  }
  console.log(`A message was deleted in ${message.channel.name} by ${user}`)
  logs.send(`the message "${message.content}" was deleted in ${message.channel.name} by ${user}`);
})

//Logs Bans
pollyBot.on('guildBanAdd', async (guild, user) => {
  const logs = pollyBot.channels.get("545079453714350103");

  const entry = await guild.fetchAuditLogs({type: 'MEMBER_BAN_ADD'}).then(audit => audit.entries.first())
    
   banner = entry.executor.username

  console.log(`${user.username} was banned by ${banner}`)
  logs.send(`${user.username} was banned by ${banner}`);
})

//Logs Unbans
pollyBot.on('guildBanRemove', async (guild, user) => {
  const logs = pollyBot.channels.get("545079453714350103");

  const entry = await guild.fetchAuditLogs({type: 'MEMBER_BAN_REMOVE'}).then(audit => audit.entries.first())
    
   banner = entry.executor.username

  console.log(`${user.username} was unbanned by ${banner}`)
  logs.send(`${user.username} was unbanned by ${banner}`);
});


