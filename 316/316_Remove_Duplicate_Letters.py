class Solution(object):
    def removeDuplicateLetters(self, s):
        self.d = {}
        res = self.removeDuplicateLettersRecursive(s)
        return res

    def removeDuplicateLettersRecursive(self, s):
        if len(s) <= 1:
            return s
        if self.d.get(s) is not None:
            return self.d[s]
        letter = s[0]
        rest_res = self.removeDuplicateLettersRecursive(s[1:])
        # print 'letter, rest_res =', letter, rest_res
        if letter in rest_res:
            rest_res_no_letter = rest_res.replace(letter, '')
            if letter + rest_res_no_letter > rest_res:
                return rest_res
            rest_no_letter = s[1:].replace(letter, '')
            res = letter + self.removeDuplicateLettersRecursive(rest_no_letter)
            self.d[s] = res
            return res
        else:
            res = letter + rest_res
            self.d[s] = res
            return res


test = Solution()
print test.removeDuplicateLetters("bcabc") # "abc"
print test.removeDuplicateLetters("cbacdcbc") # "acdb"
print test.removeDuplicateLetters("fabhfaecfadgeg") # "abhcfdeg"
print test.removeDuplicateLetters("cdadabcc") # "adbc"
print test.removeDuplicateLetters("fabhfaecfadgegh") # "abcfdegh"
print test.removeDuplicateLetters("dwzbwczdwzaydw") # "bcdwzay"
print test.removeDuplicateLetters("mitnlruhznjfyzmtmfnstsxwktxlboxutbic") # "ilrhjfyzmnstwkboxuc"
print test.removeDuplicateLetters("leetcode") # "letcod"
print test.removeDuplicateLetters("stsxwktxboxutbc") # "stwkboxuc"
print test.removeDuplicateLetters("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws") # "bfegkuyjorndiqszpcaw"
print test.removeDuplicateLetters("yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk") # "ciorhsaebpunvdyktzfjlgwq"
# print test.removeDuplicateLetters("laepnvlpndl") # "aenvlpd"
print test.removeDuplicateLetters(
    "wmxkuuoordmnpnebikzzujdpscpedcrsjphcaykjsmobturjjxxpoxvvrynmapegvtlasmyuddgxygkaztmbpkrnukbxityz"
) # "wbcdhajmoegvlskprnuxityz"
print test.removeDuplicateLetters(
    "peymrzknlxtrutjiybqemquchgvtmmtpjvunvekszrkatctcirxwuqknrycpdtcuadblzkkleduezgspoxhhssoipbmdgrqggpfdsanolzczpaggwxrlaleaqtnzxclmxwjucnujsptnbmmjzzjhypnlsoxjveywsufegzlfnyvkcnfevkshbckfropoydkdlblppllgefagjgpajsplvxknvtlgtjyhmnwxcpjjzcizihycvsnhnnmqohivekitxzuo"
) # "abcefghkrdjlmnwpiysqovtxzu"
print test.removeDuplicateLetters(
    "cruaebrnuzdmpfivugqejkspqvxxgnjixjtoboexjwcywzwptiahdbxkmhccsdnlmrmldwoxnurnlaiyzshimpzbmunvwhfkcvbeeorioxoxommgkjablxuibuxbuhhclgjwsgecuhvqscwutbownyjckhqlhjrdmtkozdwuewsxpupwhjeywznccjdeiisirvkvfroiyhhwuynmhwsdzmwauezxbssaxefktyufjnysvcmxrqxunoipqrbjxnxdwmeebpgucfxvvaansdpfetpipqynomtwkloczuepklwmhawfgovewnvxeqyghndlyoqxvoxwozfzprqwvcewvzjykyohfmywymudenrxwcoxrbsgctenzjxhqwtghlpnhkrjkxualiarouhscitxpmgabllajoqipvslibzxioocvvpdlwxvbvspezufenplebnajqsyixar"
) # "abcdefghjkiostmlpvwxzunqyr"
print test.removeDuplicateLetters(
    "yiklorymxepctlnomfmymitulgfuudxturmemjxxlloevwyfriazwyckgbfogfrppnsomjfhoobirytzzksemgrcbcegbbhaurrrlyxquuoivdcykcpnntgrktwtmgstjrvsvajfukhxwgvsvgzwoatnnzszksxstzkojmyuriyriyqkaqghoxilykyxepnsjeybgxxwyyornzxzttsylsoqlumzwlsdxvzgjfpwwoejsieeyoremvqfyekmxdsabogijmqxdruiydlkrvobwqmlmahmfpwbopbdxhinowqavdasnkeagpjvznzfmlllydgosztljnkrkpjhsqtjxjumzasfitacjqenwcskkkifgzatcevfwererjjabmmmdsnuacxzrgjyytbmxccagjbemkmemjpaqwpjdsunvmfuromfhmumhlzycbhptfjuodlgjxuxcggtotaxjlqbccghyplvtgrwwlhmriwnecdhjmbpzdaqgpyhinawvmxjyiptiroxtuwybcjjkqcirscdqbakpwdiabgirknpvlwmvspufpdqchvbqbspyznfuscidqcbtcvwsqgjjdfpnuhgpxkgikvagtbhnssycxpefsqxbcgtubdmtcojbzpcjvfoslunoiixxdakfczg"
) # "abcdefghijklmnoprqstvwuxyz"
