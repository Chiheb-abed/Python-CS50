import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    nbr = len(corpus)
    pages = {}

    if corpus[page]:
        togo = corpus[page]
        div = len(togo)
        for v in corpus:
            if v in togo:
                pages[v] = damping_factor / div
            else:
                pages[v] = 0
            pages[v] += (1-damping_factor) / nbr
    else:
        for k in corpus:
            pages[k] = 1/nbr

    return ( dict(sorted(pages.items(), key=lambda x:x[0])))



def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    samples={page : 0 for page in corpus}
    page= random.choice(list(corpus.keys()))

    for _ in range(n):

        sample = transition_model (corpus,page,damping_factor)
        choices = list(sample.keys())
        weight = list(sample.values())

        page = random.choices(choices,weights=weight)[0]
        samples[page] += 1

    for p in samples:
        samples[p] /= n

    return dict(sorted(samples.items()))







def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    keys = list(corpus.keys())
    values = list(corpus.values())

    ranks = {key : 1/len(keys)  for key in sorted(keys)}
    rank ={}
    check = 0
    s=0

    while True:
        for key in corpus:
            for k in corpus:
                if key in corpus[k]:
                    s+= ranks[k]/len(corpus[k])
            rank[key]= ((1-damping_factor)/len(keys))+(damping_factor * s)
            s=0
            if abs(rank[key] - ranks[key]) 	< 0.001 :
                check +=1
        ranks = rank
        rank ={}
        if check == len(keys):
            return ranks
        check = 0




if __name__ == "__main__":
    main()
