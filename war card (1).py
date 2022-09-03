#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[2]:


class card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit


# In[3]:


Two_Hearts =card("Hearts","Two")


# In[4]:


print(Two_Hearts)


# In[5]:


Two_Hearts.rank


# In[6]:


values[Two_Hearts.rank]


# In[7]:


Three_of_Clubs =card("Clubs","Three")


# In[8]:


print(Three_of_Clubs)


# In[9]:


Three_of_Clubs.values


# In[10]:


Two_Hearts.values < Three_of_Clubs.values


# In[11]:


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
                                


# In[12]:


new_deck = Deck()


# In[13]:


mycard = new_deck.deal_one()


# In[14]:


print(mycard)


# In[15]:


Bottom_card = new_deck.all_cards[-1]


# In[16]:


print(Bottom_card)


# In[17]:


class player:
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
    def remove_one(self):
        
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        
        return f'player {self.name} has {len(self.all_cards)} cards.'
        
    


# In[18]:


new_player = player("jose")


# In[19]:


print(new_player)


# In[20]:


new_player.add_cards(mycard)   


# In[21]:


print(new_player)


# In[22]:


mycard


# In[23]:


player_one = player("One")
player_two = player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# In[24]:


game_on = True


# In[ ]:


round_num = 0

while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    if len(player_one.all_cards) == 0:
        print('player One, out of cards!player Two wins!')
        game_on = False
        break
    
    if len(player_two.all_cards) == 0:
        print('player Two, out of cards!player One wins!')
        game_on = False
        break
    
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].values > player_two_cards[-1].values:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
            
        elif player_one_cards[-1].values < player_two_cards[-1].values:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print('war!')
            
            if len(player_one.all_cards) < 5:
                print("player one unable to declair war!")
                print("PLAYER TWO WINS!")
                game_on = False
                
            elif len(player_two.all_cards) < 5:
                print("player two unable to declair war!")
                print("PLAYER ONE WINS!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
    


# In[ ]:




