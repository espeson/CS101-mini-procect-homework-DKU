import random


class Player:
    def __init__(self, name, ht, wt, sh2_per, sh2_tot, sh3_per, sh3_tot, reb, st, bl):
        self.name = name
        self.ht = ht
        self.wt = wt
        self.sh2_per = sh2_per
        self.sh2_tot = sh2_tot
        self.sh3_per = sh3_per
        self.sh3_tot = sh3_tot
        self.reb = reb
        self.st = st
        self.bl = bl

    def __str__(self):
        return self.name

    def shoot(self):
        sh2_chance = self.sh2_tot / (self.sh2_tot + self.sh3_tot)

        if random.random() < sh2_chance:
            if random.random() < self.sh2_per:
                return 2
            else:
                return -2
        else:
            if random.random() < self.sh3_per:
                return 3
            else:
                return -3

    def steal_prob(self, opp):
        ht_diff = self.ht - opp.ht

        steal_prob = (self.st / 50) + (ht_diff / 77) * 0.05

        return steal_prob

    def steal(self, opp):
        return random.random() < self.steal_prob(opp)

    def block_prob(self, opp):
        ht_diff = self.ht - opp.ht

        block_prob = (self.bl / 50) + (ht_diff / 77) * 0.1

        return block_prob

    def block(self, opp):
        return random.random() < self.block_prob(opp)

    def rebound_prob(self, opp):
        ht_diff = self.ht - opp.ht
        wt_diff = self.wt - opp.wt

        rb_prob = 0.9 + (ht_diff / 77) * 0.1 + (wt_diff / 222) * 0.05

        return rb_prob

    def rebound(self, opp):
        return random.random() < self.rebound_prob(opp)


class Game:
    def __init__(self, p1, p2, max_pt):
        self.p1 = {'player': p1}
        self.p2 = {'player': p2}

        self.max_pt = max_pt

        self.p1['points'] = 0
        self.p1['2pt'] = 0
        self.p1['2pt_shots'] = 0
        self.p1['3pt'] = 0
        self.p1['3pt_shots'] = 0
        self.p1['steals'] = 0
        self.p1['blocks'] = 0
        self.p1['rebounds'] = 0

        self.p2['points'] = 0
        self.p2['2pt'] = 0
        self.p2['2pt_shots'] = 0
        self.p2['3pt'] = 0
        self.p2['3pt_shots'] = 0
        self.p2['steals'] = 0
        self.p2['blocks'] = 0
        self.p2['rebounds'] = 0

    def stats(self, p):
        player = self.p1
        if p == 2:
            player = self.p2

        per_3pt = 0
        if player['3pt_shots'] > 0:
            per_3pt = int(player['3pt'] / player['3pt_shots'] * 100)
        return '{} 2-pt, {} 2-pt shots ({}%), {} 3-pt, {} 3-pt shots ({}%), {} steals, {} blocks, {} rebounds'.format(
            player['2pt'],
            player['2pt_shots'],
            int(player['2pt'] / player['2pt_shots'] * 100),
            player['3pt'],
            player['3pt_shots'],
            per_3pt,
            player['steals'],
            player['blocks'],
            player['rebounds'])

    def play(self, disp=False):
        offense = self.p1
        defense = self.p2

        while offense['points'] < self.max_pt and defense['points'] < self.max_pt:

            # defense tries to steal the ball from offense
            if defense['player'].steal(offense['player']):
                defense['steals'] += 1
                if disp:
                    print(defense['player'], 'steal!')

                # offense and defense switch
                offense, defense = defense, offense
                continue

            # defense tries to block
            if defense['player'].block(offense['player']):
                defense['blocks'] += 1
                if disp:
                    print(defense['player'], 'block!')
                # offense and defense switch
                offense, defense = defense, offense
                continue
            # defense tries to steal the ball from offense
            if defense['player'].steal(offense['player']):
                defense['steals'] += 1
                if disp:
                    print(defense['player'], 'steal!')

                # offense and defense switch
                offense, defense = defense, offense
                continue
            if p1.

        if offense['points'] > defense['points']:
            return (offense, defense)
        else:
            return (defense, offense)