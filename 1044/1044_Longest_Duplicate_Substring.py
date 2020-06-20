class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        self.list_s = list(S)
        if len(set(self.list_s)) == 1:
            return ''.join(self.list_s[:-1])
        d = [{}]
        d.append({})
        for i, c in enumerate(self.list_s):
            if d[1].get(c) is None:
                d[1][c] = []
                for j, cc in enumerate(self.list_s):
                    if c == cc:
                        d[1][c].append(j)
        subs = set(c for c in self.list_s if len(d[1].get(c)) > 1)
        sub_len = 2
        while True:
            d.append({})
            for sub in subs:
                sub_locs = d[sub_len-1].get(sub)
                for loc in sub_locs:
                    new_sub = self.extend(loc, len(sub))
                    if len(new_sub) > len(sub):
                        if d[sub_len].get(new_sub) is None:
                            d[sub_len][new_sub] = [loc]
                        else:
                            d[sub_len][new_sub].append(loc)
            subs = set(sub for sub in d[sub_len].keys() if len(d[sub_len].get(sub)) > 1)
            if len(subs) == 0:
                break
            sub_len += 1
        res = set(sub for sub in d[sub_len-1].keys() if len(d[sub_len-1].get(sub)) > 1)
        if len(res) > 0:
            return res.pop()
        else:
            return ''

    def extend(self, loc, len_sub):
        return ''.join(self.list_s[loc : min(len(self.list_s), loc+len_sub+1)])

test = Solution()
print test.longestDupSubstring("banana") # 'ana'
print test.longestDupSubstring("indooroopilly") # 'oo'
print test.longestDupSubstring("wollongong") # 'ong'
print test.longestDupSubstring("waggawagga") # 'wagga'
print test.longestDupSubstring("abcd") # ''
print test.longestDupSubstring("aaaaaaaa") # 'aaaaaaa'
print test.longestDupSubstring("abababab") # 'ababab'
print test.longestDupSubstring("aaaaaaaabababab") # 'aaaaaaa'
print test.longestDupSubstring(
'unuoqslvgaekunapeaapsxbodakcrapmmfuxoowlysenyiygzhawbfbuxlswtxzzhlspfgzckzuoxizijrluvndcpnknsvrnfulksqqxdznfjgjlocozuolroealyhhwrzcsuzgcsekkqmwlnylsscpmynjchwvpwebwkraudfqboeqmxhghekcstrcozldbwyniwqmyrbkzwvknulehzxwckwohlmjvlqyexvzzlptbnnbctywyezcssubmiukcsixmnapgttmlfwtwnmxqgsobqsnxucwrszxcuprnlxjteytwqzridgtgkkbsekeytuxslavhebbpjewdwlhchtzwohqkojiqneahxacutymteoyloottnsmmrphngclortfvudoeckxkjqatxqmvboumxmdrxoxpyprkwvfpviqkbhsjdeosxdbzzfsomrxojkokofrrdoavhjufyayisibcgngqprircpcjyvynhzmrtyynfgfgeomscywbcvmlhcmyesuxwurmpdxhddyfnumgkvphmtqzrbsbjeliyrqfswrchkurvqtsmzchjfvotdmueabpllagtfvefssmgevrzydftuvxqdbdrpysifoxgvlkljhkiksoxfndxayrsaxeoefmimnqfeerggwxsbyarfvfwvrmtwjainqposafhwysxaaegzeewhyrsfnduqihpwipeewnubscqpvjekikyiwmpwynydbnvylqydgiwsenvulkknlbuqpwhxqclrnuvdwqpxkksyewsklffwtggbmxnttvnjbiqjdoezffmmighfdcirjakacncwckjqwqsjxsbsxbaeaagmnybxpwvucyskfkydlkxdlfmodygcxzimmhdgmwwqxrflldkwvyqlfwasxxoetlgtopmqnfkfvkshkrikfcvdrguxciupphxyssowakrnsiutntlliedxnqkldzfkqefgvyaargpqbknlmlbejkuupolrhapowrgciyteeeulpldvlqkklwsxtvcmxjozbfqgmslutnkspfoaeylxufmuropnafrjveufqymddcrzvbdkhghzvbjzxyuibkemslbsluzwnduiutluergimcjsziusnqhyazuhskekblpoexmurndswlwxwieujdyilfntaaphwvnauvwmihlfphfpxzkwinxitiqxamjqxtdxswgxfmsfuqwtqqnzracsoerlrntgyypdroiuqtiawxeogqcrxxbjmgkqrlrbgeglkamqfvgaiipuxcvllcujnnlfzidrvzowaupaucbxzwzhueqqdphpmsdszdtcycrmiwyhslbvknlxhfgpcbotvarakaymjgfydzfmnxwausfhdxulmxhvzgbswfdwrtitwyibwfnpsekmymsglzpiyrhnuaatmqkjqhcwycnaxjbxqgprgoesjnupyfhbyounmbwgjfplslyudxyaxuspyxjcuorzxcryiuwlgprpurjdxozsalkbjcjatnxstbxinrokiufjldyuyngkiobomuemplhziwaapevhrluxohodizmmqznpbggcaqfgobgpvytmbpdmrrcbzbgrppmlmigghuzrdfhwhksgmmnjnbglrrckwbdstsjdjxaeopxawedvszchktinhceceauookzcwbdkbglzkedrjuqhrnaxluttcjbbdmqimlgppvuvmjqipkcjvyzhingwymthqrpguhvlcjqrstczkdvdrwwtwdrakmbxzjfsszpziurglmpsyllgxtbewoftnhvzmtygsvbnwhltwqszqdopzxbwyrdyrpffnilfdxtlofyicjshyrpncsqndubqkgkgrtbybulwegugcvfqhpfnvvccocolfpiyojgoranoyegkpitmfkmdkyihdqscwykyhgkyljypjobeijjvdpjglbkefxtsmyyytluqpvdcsgrtvsamzupdjyzqtcvpoquialxzaeerxtqkitsapniklylrztgclbxyzzrkanhucwdccdvafyirulajxbmeyaoqtqpprkohdddzdxtiwwctcevneriqahvrgyqvyrwfcvvqbhxmiajqkwhztepimveqisonqccfgwnhpkkqsqlmqqszwjxcpmyzldhjmriayuxpfosdtmhvtncuboiggyroxgwlbybievmdwaverpetzrmeogojuyipkwsibihuhzxjnwugjpwonfsbwaxfcqveyipwkhkzsfarvxrdlxvoiduextlcnnwuaiishdbfnxvfzkqfbqynfznbqijfkamnhlwcmkysbotlebtyfkoptfignbwxfldmbebmtyoggfvbyyygbibfhgfrdtwptwihjndlxmtdkntxtfjwstbmukwlwkzecogozerskubaxjqtliwpgyfwvkqqagmwmnfvuoujlelopdbfqyjnemaibfmgfhqzoptcolufrgafmwkzlxaudgvkhicwjdyomiqgoapvhyakslmhnznivjulyyqusxolkmfyskcfgshotfdjbtmflvtagraeazawnbtcquiivziijjporrsuytdkayjtnexvwtoswqmncbvwsxcaowrjmqdtyzqdjrqbmnaqqlkbdsrweeofeztqlgijzsriayrlknxcinibqqguxztuikzetcwipuchwukczxunuoqslvgaekunapeaapsxbodakcrapmmfuxoowlysenyiygzhawbfbuxlswtxzzhlspfgzckzuoxizijrluvndcpnknsvrnfulksqqxdznfjgjlocozuolroealyhhwrzcsuzgcsekkqmwlnylsscpmynjchwvpwebwkraudfqboeqmxhghekcstrcozldbwyniwqmyrbkzwvknulehzxwckwohlmjvlqyexvzzlptbnnbctywyezcssubmiukcsixmnapgttmlfwtwnmxqgsobqsnxucwrszxcuprnlxjteytwqzridgtgkkbsekeytuxslavhebbpjewdwlhchtzwohqkojiqneahxacutymteoyloottnsmmrphngclortfvudoeckxkjqatxqmvboumxmdrxoxpyprkwvfpviqkbhsjdeosxdbzzfsomrxojkokofrrdoavhjufyayisibcgngqprircpcjyvynhzmrtyynfgfgeomscywbcvmlhcmyesuxwurmpdxhddyfnumgkvphmtqzrbsbjeliyrqfswrchkurvqtsmzchjfvotdmueabpllagtfvefssmgevrzydftuvxqdbdrpysifoxgvlkljhkiksoxfndxayrsaxeoefmimnqfeerggwxsbyarfvfwvrmtwjainqposafhwysxaaegzeewhyrsfnduqihpwipeewnubscqpvjekikyiwmpwynydbnvylqydgiwsenvulkknlbuqpwhxqclrnuvdwqpxkksyewsklffwtggbmxnttvnjbiqjdoezffmmighfdcirjakacncwckjqwqsjxsbsxbaeaagmnybxpwvucyskfkydlkxdlfmodygcxzimmhdgmwwqxrflldkwvyqlfwasxxoetlgtopmqnfkfvkshkrikfcvdrguxciupphxyssowakrnsiutntlliedxnqkldzfkqefgvyaargpqbknlmlbejkuupolrhapowrgciyteeeulpldvlqkklwsxtvcmxjozbfqgmslutnkspfoaeylxufmuropnafrjveufqymddcrzvbdkhghzvbjzxyuibkemslbsluzwnduiutluergimcjsziusnqhyazuhskekblpoexmurndswlwxwieujdyilfntaaphwvnauvwmihlfphfpxzkwinxitiqxamjqxtdxswgxfmsfuqwtqqnzracsoerlrntgyypdroiuqtiawxeogqcrxxbjmgkqrlrbgeglkamqfvgaiipuxcvllcujnnlfzidrvzowaupaucbxzwzhueqqdphpmsdszdtcycrmiwyhslbvknlxhfgpcbotvarakaymjgfydzfmnxwausfhdxulmxhvzgbswfdwrtitwyibwfnpsekmymsglzpiyrhnuaatmqkjqhcwycnaxjbxqgprgoesjnupyfhbyounmbwgjfplslyudxyaxuspyxjcuorzxcryiuwlgprpurjdxozsalkbjcjatnxstbxinrokiufjldyuyngkiobomuemplhziwaapevhrluxohodizmmqznpbggcaqfgobgpvytmbpdmrrcbzbgrppmlmigghuzrdfhwhksgmmnjnbglrrckwbdstsjdjxaeopxawedvszchktinhceceauookzcwbdkbglzkedrjuqhrnaxluttcjbbdmqimlgppvuvmjqipkcjvyzhingwymthqrpguhvlcjqrstczkdvdrwwtwdrakmbxzjfsszpziurglmpsyllgxtbewoftnhvzmtygsvbnwhltwqszqdopzxbwyrdyrpffnilfdxtlofyicjshyrpncsqndubqkgkgrtbybulwegugcvfqhpfnvvccocolfpiyojgoranoyegkpitmfkmdkyihdqscwykyhgkyljypjobeijjvdpjglbkefxtsmyyytluqpvdcsgrtvsamzupdjyzqtcvpoquialxzaeerxtqkitsapniklylrztgclbxyzzrkanhucwdccdvafyirulajxbmeyaoqtqpprkohdddzdxtiwwctcevneriqahvrgyqvyrwfcvvqbhxmiajqkwhztepimveqisonqccfgwnhpkkqsqlmqqszwjxcpmyzldhjmriayuxpfosdtmhvtncuboiggyroxgwlbybievmdwaverpetzrmeogojuyipkwsibihuhzxjnwugjpwonfsbwaxfcqveyipwkhkzsfarvxrdlxvoiduextlcnnwuaiishdbfnxvfzkqfbqynfznbqijfkamnhlwcmkysbotlebtyfkoptfignbwxfldmbebmtyoggfvbyyygbibfhgfrdtwptwihjndlxmtdkntxtfjwstbmukwlwkzecogozerskubaxjqtliwpgyfwvkqqagmwmnfvuoujlelopdbfqyjnemaibfmgfhqzoptcolufrgafmwkzlxaudgvkhicwjdyomiqgoapvhyakslmhnznivjulyyqusxolkmfyskcfgshotfdjbtmflvtagraeazawnbtcquiivziijjporrsuytdkayjtnexvwtoswqmncbvwsxcaowrjmqdtyzqdjrqbmnaqqlkbdsrweeofeztqlgijzsriayrlknxcinibqqguxztuikzetcwipuchwukczx'
)