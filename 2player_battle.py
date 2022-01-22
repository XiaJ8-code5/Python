import os,time,random
os.system ('cls||clear')

while True:
	print ('\n来了老弟~, 开始负相桑害~!')
	player_win = 0
	enemy_win = 0
	for round in range(1,4):
		player_life = random.randint(100,150)
		player_attack = random.randint(30,50)
		enemy_life = random.randint(100,150)
		enemy_attack = random.randint(30,50)
		time.sleep(1)
		print (f'''\n=== Round number {round} ===
Player:
HP: {player_life}
Att: {player_attack}\n
Enemy:
HP: {enemy_life}
Att: {enemy_attack}
====================''')
	
		while player_life > 0 and enemy_life >0:
			player_life = player_life - enemy_attack
			enemy_life = enemy_life - player_attack
			time.sleep(1)
			print (f'-- Player attacked, enemy HP left: {enemy_life}')
			print (f'-- Enemy attacked, player HP left: {player_life}\n')
			
		if player_life > 0 and enemy_life <= 0:
			print ('-- Player wins this round.')
			player_win += 1
		elif enemy_life > 0 and player_life <= 0:
			print ('-- Enemy wins this round.')
			enemy_win += 1
		else:
			print ("-- Both dead, it's a draw.")
	
	time.sleep(1)
	print (f'''\n=== Final Score ===
	
Player win: {player_win}
Enemy win: {enemy_win}\n''')
	
	if player_win > enemy_win:
		print ('Player is the final winner.')
	elif player_win < enemy_win:
		print ('Enemy is the final winner.')
	else:
		print ("It's a draw, play again.")
	print ('=' * 20+'\n')
	
	play_again = input('\n老铁再来一局?: [Y/N]')
	if str.upper(play_again) == 'Y':
		continue
	else:
		print ('\n拜拜~')
		break
	
