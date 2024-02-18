#!/usr/bin/env python

import sys
import numpy as np

if len(sys.argv) < 2:
    print('Usage: normalized-summary-score.py responses.csv all_abstracts.csv')
    sys.exit(1)

review_dtype = np.dtype({'names': ('timestamp', 'reviewer', 'id', 'gis', 'edu', 'astro',
            'bio', 'geophys', 'viz', 'soc', 'eng','novelty', 'general', 
            'structure', 'links','comment'),
            'formats': ('S22', 'S32', 'S22', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4',
                'f4', 'f4', 'f4', 'f4','S512')})
summary_score_dtype = np.dtype({'names': ('id', 'gis', 'edu', 'astro',
            'bio', 'geophys', 'viz', 'soc','eng','overall', 'n_reviews','comment'),
            'formats': ('S22', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4', 'f4',
                'f4', 'i4','S512')})
non_norm_cats = 'gis', 'edu', 'astro', 'bio', 'geophys', 'viz', 'soc', 'eng'
norm_cats = 'novelty', 'general', 'structure', 'links'
norm_cats_weights = ({'novelty':2.0/8.0, 'general':4.0/8.0, 'structure':1.0/8.0, 'links':1.0/8.0})

reviews = np.loadtxt(sys.argv[1],
        delimiter=',', dtype=review_dtype)

reviewers = dict.fromkeys(reviews['reviewer'], np.array([],dtype=review_dtype))
for review in reviews:
    reviewer = review['reviewer']
    comment = review['comment']
    current_reviews = reviewers[reviewer]
    concat_reviews = np.concatenate((current_reviews, [review]))
    reviewers[reviewer] = concat_reviews

ids = dict.fromkeys([s.lower().strip() for s in reviews['id']], np.array([], dtype=review_dtype))
print('There are ' + str(len(ids)) + ' ids')
for review in reviews:
    _id = review['id'].lower().strip()
    current_reviews = ids[_id]
    concat_reviews = np.concatenate((current_reviews,[review]))
    ids[_id] = concat_reviews

summary_scores = np.zeros((len(ids),), dtype=summary_score_dtype)
ii = 0
for _id, id_reviews in ids.iteritems():
    summary_scores[ii]['id'] = _id

    for category in non_norm_cats:
        for review in id_reviews:
            reviewer = review['reviewer']
            reviewer_reviews = reviewers[reviewer]
            summary_scores[ii][category] += review[category]
        summary_scores[ii][category] /= len(id_reviews)

    for category in norm_cats:
        for review in id_reviews:
            reviewer = review['reviewer']
            reviewer_reviews = reviewers[reviewer]
            reviewer_mean = np.mean(reviewer_reviews[category])
            reviewer_std = np.std(reviewer_reviews[category])
            if reviewer_std != 0.0:
                summary_scores[ii]['overall'] += norm_cats_weights[category]*(review[category] - reviewer_mean)/reviewer_std
    summary_scores[ii]['overall'] /= len(id_reviews)
    summary_scores[ii]['n_reviews'] = len(id_reviews)
    summary_scores[ii]['comment'] = id_reviews['comment']

    ii += 1

abstract_dtype = np.dtype({'names': ('id', 'speaker', 'title', 'category', 'domain', 'type'),
            'formats': ('I4', 'S32', 'S32', 'S32', 'S32', 'S32')}) 

abstracts = np.loadtxt(sys.argv[2], delimiter=',', dtype=abstract_dtype)

with open('merged_table.csv', 'w') as fp:
    for name in abstract_dtype.names:
        fp.write(name + ',')
    for name in summary_score_dtype.names:
        fp.write(name + ',')
    fp.write('\n')
    for abstract in abstracts:
        idnum = abstract['id']
        for name in abstract_dtype.names:
            fp.write(str(abstract[name]) + ',')
        for score in summary_scores:
            if int(score['id']) == idnum:
                print("does "+str(score['id'])+" = "+str(idnum))
                for name in summary_score_dtype.names:
                    fp.write(str(score[name]) + ',')
        fp.write('\n')
