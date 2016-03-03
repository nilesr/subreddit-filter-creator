# Subreddit Filter Creator

I created this for use on /r/freegamesonsteam, but it can be applied to any subreddit. Simply put the name of each filter and the selector in the filters list, which you can expand or shrink depending on your needs. Run the script and put the first half in your stylesheet and the second half in your wiki page.

To ensure that your wiki page looks nice I recommend putting the following code in your stylesheet as well

	.wiki-page .wiki-page-content a[href='/wiki_table_true'] {
		background-color: #b1ffcd;
		color: black !important;
		text-decoration: none !important;
		cursor: text !important;
		display:block;
		width:100%;
	}

	.wiki-page .wiki-page-content a[href='/wiki_table_false'] {
		background-color: #ffcccc;
		color: black !important;
		text-decoration: none !important;
		cursor: text !important;
		display:block;
		width:100%;
	}
