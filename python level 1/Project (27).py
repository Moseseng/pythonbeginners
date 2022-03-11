# open tag
import re
re.search('<[^/>][^>]*>', '<table>') != None
True
import re
re.search('<[^/>][^>]*>', '<a href="#label">') != None
True
import re
re.search('<[^/>][^>]*>', '<img src="/img">') != None
True
import re
re.search('<[^/>][^>]*>', '</table>') != None
False

# close tag
import re
re.search('</[^>]+>', '</table>') != None
True

# self close
import re
re.search('<[^/>]+/>', '<br />') != None
True
