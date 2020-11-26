# from player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name):
        found_player = [player for player in self.players if player.name == player_name]

        if found_player:
            found_player = found_player[0]
            self.players.remove(found_player)
            found_player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        info = f"Guild: {self.name}\n"

        for player in self.players:
            info += f"{player.player_info()}" #removed \n

        return info


# player = Player("George", 50, 100)
# ivan = Player("Ivan", 69, 420)
# print(ivan.player_info())
# print(player.add_skill("Shield Break", 20))
# print(player.add_skill("Shield Break", 30))
# print(player.player_info())
# guild = Guild("UGT")
# LOL_guild = Guild("ok_nice")
# print(guild.assign_player(player))
# print(guild.assign_player(ivan))
# print(LOL_guild.assign_player(ivan))
# print(guild.guild_info())
# print(LOL_guild.guild_info())