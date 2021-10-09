# Assignment 2


## Installation

Import in the project
```python
from scraper import news
```

## Usage

Make class instance in your project


```python
# Scrapper
scrapper = news()
# Method recieves name of the coin and the amount of articles to fetch
articles = scrapper.getNews("bitcoin",1)
```

Articles are arrays of paragraphs.
```python
articles[0] # Would be an array of paragraphs
```

## Examples

```python
from scraper import news

if __name__ == '__main__':
    scrapper = news()
    articles = scrapper.getNews("bitcoin",1)
    for n in articles[0]:
        print(n)
```
## License
[MIT](LICENSE.md)
