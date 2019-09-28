# DataBuri (stil in beta version)
[![](https://travis-ci.org/codeforthailand/databuri.svg?branch=master)][travis]

All-in-one Python package for Thailand's public APIs.

This package aims to provide a unified interface to retrieve data from Thailand's public data APIs or datasets with minimum configurations needed.

The package has 2 major parts: datasource & dataset.

1. Datasource is related to public APIs. Most likely, every module in this part is developed for each data API. Mostly likely, these modules are just REST clients with options to specify authentication keys.

2. Dataset is mainly for static datasets, mainly for training ML algorithms.

**Remark:** DataBuri is still under development. A couple of functionalities
have been implemented but their signatures might be changed without any annoucement.

## Installation
```
$ pip install databuri
```

## APIs Implemented
| Name | Description |
|---|---|
| [GovSpending](https://govspending.data.go.th/api/documentation) | Thai government procurement projects |
| [Air4Thai](http://air4thai.pcd.go.th/webV2/history)  | Air quality measurements in Thailand |

### APIs to be included
- https://api-portal.sec.or.th/apidesc
- http://opend.openservice.in.th/opend/
- http://dolwms.dol.go.th/tvwebp/
- https://data.moc.go.th
- ข้อมูลนิติบุคคล จาก กรมการค้าภายใน

## Development
### Release
1. Bump version
    ```
    $ bumpversion [major|minor|patch]
    $ git push && git push --tags
    ```
2. Publish to pypi
    ```
    $ ./scripts/publish.sh <tag>
    ```
### Build documentation
1. cd `./docs`
2. `make html && ./autogen.sh`

## Related Links:
- [Project Proposal](https://docs.google.com/document/d/1XXuRovZ3bRGC18MQluO5zsZJ_6TM9COwCgRoWv6lsnM/edit?usp=sharing)

[travis]: https://travis-ci.org/codeforthailand/databuri
