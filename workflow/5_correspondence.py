from lingrex.copar import CoPaR

cop = CoPaR(
        'D_Chen_crossids.tsv',
        ref='crossids',
        fuzzy=True,
        segments='tokens'
        )
cop.get_sites(minrefs=3, structure='structure')
cop.cluster_sites()
cop.sites_to_pattern()
cop.add_patterns()
cop.write_patterns('D_patterns_Chen.tsv')
cop.output('tsv', filename='D_Chen_patterns', prettify=False)
