from lingrex.copar import CoPaR

cop = CoPaR(
        'chen-crossids.tsv', 
        ref='crossids', 
        fuzzy=True,
        segments='segments'
        )
cop.get_sites(minrefs=3, structure='structure')
cop.cluster_sites()
cop.sites_to_pattern()
cop.add_patterns()
cop.write_patterns('patterns-chen.tsv')
cop.output('tsv', filename='chen-patterns', prettify=False)   
