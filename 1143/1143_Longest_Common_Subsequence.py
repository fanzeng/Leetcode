class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        self.d = {}
        return self.longestCommonSubsequenceDP(text1, text2)

    def longestCommonSubsequenceDP(self, text1, text2):
        if text1 is None or text2 is None or len(text1) == 0 or len(text2) == 0:
            return  0
        self.d[len(text1)-1, len(text2)-1] = int(text1[-1] == text2[-1])
        for j in xrange(len(text2) - 2, -1, -1):
            self.d[len(text1)-1, j] = max(self.d[len(text1)-1, j+1], int(text1[-1] == text2[j]))
        for i in xrange(len(text1)-2, -1, -1):
            self.d[i, len(text2)-1] = max(self.d[i+1, len(text2)-1], int(text1[i] == text2[-1]))
            for j in xrange(len(text2)-2, -1, -1):
                if text2[j] == text1[i]:
                    res = self.d[i+1, j+1] + 1
                    # there is no need to max it with self.d[i, j+1] and self.d[i+1, j],
                    # because when text2[j] == text1[i],
                    # the max possible value of self.d[i, j] is self.d[i+1, j+1] + 1, i.e., you can gain at most 1 from there
                    # and this value is always achievable by consuming the char in both strings,
                    # so no need for more conditions, just simply add 1.

                    # the reason why you can only gain at most 1:
                    # if otherwise, the only possible way to gain 2 is for text2[j] to match some char in text[i+1:],
                    # and text1[i] to match some char in text2[j+1:],
                    # since text2[j] == text1[i], all these 4 chars are the same char
                    # so we have at most 2 pairs, from which we can gain at most 2.
                    # but that gain of 1 from the other pair has already been counted in
                    # self.d[i+1, j+1] by definition of this algorithm,
                    # if you look at this algorithm, when i and j match the location of those two chars, that 1 has been
                    # added right here on this very line.
                    # so in order not to double count, we should gain at most 1 here,
                    # and this is done by matching text1[i] and text2[j].
                else:
                    res = max(self.d[i+1, j], self.d[i, j+1])
                self.d[i, j] = res
                # print i, j, res

        return self.d[0, 0]
# recursive version, does not work for long strings: maximum recursion depth exceeded
    # def longestCommonSubsequenceDP(self, text1, text2):
    #     if text1 is None or text2 is None or len(text1) == 0 or len(text2) == 0:
    #         return 0
    #     if self.d.get(text1 + text2) is not None:
    #         return self.d.get(text1 + text2)
    #     c1 = text1[0]
    #     pos_c2 = text2.find(c1)
    #     if pos_c2 == -1:
    #         res_include = 0
    #     else:
    #         if len(text1) > 1:
    #             remain_1 = text1[1:]
    #         else:
    #             remain_1 = None
    #         if len(text2) > pos_c2+1:
    #             remain_2 = text2[pos_c2+1:]
    #         else:
    #             remain_2 = None
    #         res_include = 1 + self.longestCommonSubsequenceDP(remain_1, remain_2)
    #     res_not_include = self.longestCommonSubsequenceDP(text1[1:], text2)
    #     res = max(res_include, res_not_include)
    #     self.d[text1 + text2] = res
    #     return res


test = Solution()
print test.longestCommonSubsequence("abdefghij", "adbaceghj") # 6
print test.longestCommonSubsequence("abcde", "ace") # 3
print test.longestCommonSubsequence("abc", "abc") # 3
print test.longestCommonSubsequence("abc", "def") # 0

print test.longestCommonSubsequence(
    "whydynkfslsrmvyhonyjenyrenojofafmnafmfyhyjebwhqpwh",
    "ctqdkfctanypmxqxktqfwfgnwjqpsbgpydovufgfqbyvqpufujy"
)
print test.longestCommonSubsequence(
    "fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxozkpgtgtsjobujezgrkvevklmludgtyrmjaxyputqbyxqvupojutsjwlwluzsbmvyxifqtglwvcnkfsfglwjwrmtyxmdgjifyjwrsnenuvsdedsbqdovwzsdghclcdexmtsbexwrszihcpibwpidixmpmxshwzmjgtadmtkxqfkrsdqjcrmxkbkfoncrcvoxuvcdytajgfwrcxivixanuzerebuzklyhezevonqdsrkzetsrgfgxibqpmfuxcrinetyzkvudghgrytsvwzkjulmhanankxqfihenuhmfsfkfepibkjmzybmlkzozmluvybyzsleludsxkpinizoraxonmhwtkfkhudizepyzijafqlepcbihofepmjqtgrsxorunshgpazovuhktatmlcfklafivivefyfubunszyvarcrkpsnglkduzaxqrerkvcnmrurkhkpargvcxefovwtapedaluhclmzynebczodwropwdenqxmrutuhehadyfspcpuxyzodifqdqzgbwhodcjonypyjwbwxepcpujerkrelunstebopkncdazexsbezmhynizsvarafwfmnclerafejgnizcbsrcvcnwrolofyzulcxaxqjqzunedidulspslebifinqrchyvapkzmzwbwjgbyrqhqpolwjijmzyduzerqnadapudmrazmzadstozytonuzarizszubkzkhenaxivytmjqjgvgzwpgxefatetoncjgjsdilmvgtgpgbibexwnexstipkjylalqnupexytkradwxmlmhsnmzuxcdkfkxyfgrmfqtajatgjctenqhkvyrgvapctqtyrufcdobibizihuhsrsterozotytubefutaxcjarknynetipehoduxyjstufwvkvwvwnuletybmrczgtmxctuny",
    "nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjkvevgdovazmbgtqfwvejczsnmbchkdibstklkxarwjqbqxwvixavkhylqvghqpifijohudenozotejoxavkfkzcdqnoxydynavwdylwhatslyrwlejwdwrmpevmtwpahatwlaxmjmdgrebmfyngdcbmbgjcvqpcbadujkxaxujudmbejcrevuvcdobolcbstifedcvmngnqhudixgzktcdqngxmruhcxqxypwhahobudelivgvynefkjqdyvalmvudcdivmhghqrelurodwdsvuzmjixgdexonwjczghalsjopixsrwjixuzmjgxydqnipelgrivkzkxgjchibgnqbknstspujwdydszohqjsfuzstyjgnwhsrebmlwzkzijgnmnczmrehspihspyfedabotwvwxwpspypctizyhcxypqzctwlspszonsrmnyvmhsvqtkbyhmhwjmvazaviruzqxmbczaxmtqjexmdudypovkjklynktahupanujylylgrajozobsbwpwtohkfsxeverqxylwdwtojoxydepybavwhgdehafurqtcxqhuhkdwxkdojipolctcvcrsvczcxedglgrejerqdgrsvsxgjodajatsnixutihwpivihadqdotsvyrkxehodybapwlsjexixgponcxifijchejoxgxebmbclczqvkfuzgxsbshqvgfcraxytaxeviryhexmvqjybizivyjanwxmpojgxgbyhcruvqpafwjslkbohqlknkdqjixsfsdurgbsvclmrcrcnulinqvcdqhcvwdaxgvafwravunurqvizqtozuxinytafopmhchmxsxgfanetmdcjalmrolejidylkjktunqhkxchyjmpkvsfgnybsjedmzkrkhwryzan"
)