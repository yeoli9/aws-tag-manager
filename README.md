# aws-tag-manager

## Description

- Simple
- Automatically, attach tag to your aws resources.
- Please modify and use the original code appropriately.
- support runtimes: Python3.x

## Usage

### use case 1

- eventBridge Scheduler - lambda(tag-manager)
     ㄴ--- ('0 * * * *')     ㄴ---- parameter-store (or secrets manager)

### use case 2
