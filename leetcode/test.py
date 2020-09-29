import codecs
import collections
with codecs.open('/Users/wangming/Desktop/slot_corpus_details.txt','r') as fr, \
    codecs.open('/Users/wangming/Desktop/temp.txt','w') as fw:
    cnt = collections.defaultdict(int)
    for line in fr:
        splits = line.strip('\n').split(',')
        domain = splits[1].strip()
        intent = splits[2].strip()
        if domain == 'video' and intent == 'play':
            # if domain not in ['video']: continue
            slot = splits[3].strip()
            val = int(splits[4])
            key = (intent, slot)
            cnt[key]+=val

    for k,v in cnt.items():
        fw.write('{},{},{}\n'.format(k[0],k[1],v))
