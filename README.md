# Data·Buri
[![](https://travis-ci.org/codeforthailand/databuri.svg?branch=master)][travis]

All-in-one Python package for Thailand's public APIs

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

## Related Links:
- [Project Idea](https://github.com/codeforthailand/org/issues/2)
- [Project Proposal](https://docs.google.com/document/d/1XXuRovZ3bRGC18MQluO5zsZJ_6TM9COwCgRoWv6lsnM/edit?usp=sharing)

[travis]: https://travis-ci.org/codeforthailand/databuri