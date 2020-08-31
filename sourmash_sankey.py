from charcoal import utils
import sourmash
from sourmash.lca import taxlist, LineagePair
import collections

import plotly.graph_objects as go


class GenomeSankeyFlow:
    "Build and track 'flow' of hash/k-mer idents across taxonomic ranks."
    def __init__(self):
        # index for lineages
        self.next_index = 0
        self.index_d = {}

        # src/dest connections for links in sankey diagram
        self.links_d = {}

        # build the set of (rank1, rank2) for all pairs; stop at species.
        taxlist_pairs = []
        for rank in taxlist():
            if rank == 'superkingdom':
                last_rank = rank
                continue
            if rank == 'species':
                break
            taxlist_pairs.append((last_rank, rank))
            last_rank = rank
        self.taxlist_pairs = tuple(taxlist_pairs)

        # build a lineage w/unassigned at each rank for potential use.
        unassigned_lin = []
        for rank in taxlist():
            if rank == 'species':
                break
            unassigned_lin.append(LineagePair(rank, 'unassigned'))

        self.unassigned_lin = tuple(unassigned_lin)

    def get_index(self, lin):
        "For the given lineage, return or create & return unique index."
        lin = tuple(lin)
        if lin not in self.index_d:
            self.index_d[lin] = self.next_index
            self.next_index += 1
        return self.index_d[lin]

    def make_labels(self):
        "Make the labels in index order."
        linlist = list(self.index_d.items())
        linlist.sort(key = lambda x: x[1])
        return [ lin[-1].name for lin, idx in linlist ]

    def add_link(self, lin, count, src_rank, dest_rank, color):
        "build a link for lineage from src_rank to dest_rank. Use color/count."
        src_lin = utils.pop_to_rank(lin, src_rank)
        dest_lin = utils.pop_to_rank(lin, dest_rank)
        
        dest = self.get_index(dest_lin)
        src = self.get_index(src_lin)
        d1 = self.links_d.get(src, {})
        (prev_color, total_count) = d1.get(dest, (color, 0))
        total_count += count

        assert color == prev_color, (color, prev_color)

        d1[dest] = (color, total_count)
        self.links_d[src] = d1

    def make_links(self, genome_lineage, counts, show_unassigned=False):
        "Put all of the links together."
        # collect the set of lineages to display
        # note: could add a filter function to focus in on a specific 'un
        genus_lins = set(counts.keys())
        if not show_unassigned:
            if self.unassigned_lin in genus_lins:
                genus_lins.remove(self.unassigned_lin)

        for lin in genus_lins:
            count = counts[lin]
            for last_rank, rank in self.taxlist_pairs:
                rank_lin = utils.pop_to_rank(lin, rank)

                color = "lightgrey"
                if utils.is_lineage_match(genome_lineage, lin, rank):
                    color = "lightseagreen"
                self.add_link(lin, count, last_rank, rank, color)
                last_rank = rank
                
    def make_lists(self):
        "Construct lists suitable for handing to plotly link."
        src_l = []                        # source of link
        dest_l = []                       # destination link
        cnt_l = []                        # size/count of link
        color_l = []                      # color of link
        label_l = []                      # label for link

        # track sum of all counts, so we can turn into percent
        sum_counts = 0
        for k in sorted(self.links_d):
            for j in sorted(self.links_d[k]):
                sum_counts += self.links_d[k][j][1]

        # now, put together set of links.
        for k in sorted(self.links_d):
            for j in sorted(self.links_d[k]):
                # note here that the indices in links_d are indices into
                # labels.
                src_l.append(k)
                dest_l.append(j)

                # retrieve color & counts...
                color, counts = self.links_d[k][j]
                color_l.append(color)    
                cnt_l.append(counts)

                # calculate percent of counts.
                pcnt = counts / sum_counts * 100
                label_l.append(f'{pcnt:.1f}% of total k-mers')                
               
        return src_l, dest_l, cnt_l, color_l, label_l
    
    def make_plotly_fig(self, title):
        "Build a plotly figure/sankey diagram."
        # make the data to go into the sankey figure.
        labels = self.make_labels()
        src_l, dest_l, cnt_l, color_l, label_l = self.make_lists()

        # build figure
        fig = go.Figure(data=[go.Sankey(
            node = dict(
              pad = 15,
              thickness = 20,
              line = dict(color = "black", width = 0.5),
              label = labels,
              color = "blue"
            ),
            link = dict(
              source = src_l,
              target = dest_l,
              value = cnt_l,
              color = color_l,
              label = label_l,
          ))])

        if title:
            fig.update_layout(title_text=title, font_size=10)

        return fig
    
