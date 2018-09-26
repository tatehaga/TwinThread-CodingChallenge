#!/usr/bin/python3
import json
import urllib.request


url = "https://www.twinthread.com/code-challenge/assets.txt"

print("Downloading assets...")

# with/as automatically closes open files at end of use
with urllib.request.urlopen(url) as read_file:
    data = json.load(read_file)
print("Done.\n")

# 3 high level labels: asset_status, dataType, assets
asset_status = data.get("asset_status")
dataType = data.get("dataType")
assets = data.get("assets") # creates a list of asset dictionaries


# prints assets in their entirety
def printAsset(asset):
    for criteria in asset:
        print(criteria + ": " + str(asset.get(criteria)))


# prints minimal form of assets, just id number and name
def printAssetMin(asset):
    print(str(asset.get("assetId")) + ": " + asset.get("name"))


# search through assets based on search criteria
def assetSearch(asset, complete, status):
    for tags in asset:
        if tags == criteria:
            if query == str(asset.get(criteria)):
                if complete:
                    printAsset(asset)
                    print()
                else:
                    printAssetMin(asset)
                    print()
                status = True
    return status

def getChildren(assetId):
    retlist = []
    for asset in assets:
        if asset.get("parentId") == assetId:
            retlist.append(asset.get("assetId"))
    return retlist


# Main loop

while True:
    command = input("Enter command (or help for list of commands) ")

    # unfortunately, Python has no switch/case functionality, so if/elif/else statements it is

    if command.lower() == "help":
        print("Commands:\n "
              "search: search asset data by name, description, or other field, displays asset id and name\n "
              "search complete: search asset data by name, description, or other field, displays asset id and name\n "
              "list: gives a list of all assets that have a critical status, displays asset id and name\n "
              "list complete: gives a list of all assets that have a critical status and displays complete asset "
              "information\n " 
              "classes: provides a count of distinct class names, then lists assets that contain those class names\n "
              "tree: generates a hierarchy for a given asset id\n "
              "exit: closes the application\n "
              "help: gives list of valid commands\n")

    elif command.lower() == "exit":
        break

    elif command.lower() == "list complete":
        print("Critical assets:\n")
        for asset in assets:
            if asset.get("status") == asset_status.get("critical"):
                printAsset(asset)
                print()

    elif command.lower() == "list":
        print("Critical assets: (assetId: name)\n")
        for asset in assets:
            if asset.get("status") == 3:
                printAssetMin(asset)
                print()

    elif command.lower() == "search":
        criteria = input("Search by (name, assetId, description, etc.): ")
        query = input("Search query: ")
        print()
        found = False
        for asset in assets:
            found = assetSearch(asset, False, found)
        if not found:
            print("Not found!\n")

    elif command.lower() == "search complete":
        criteria = input("Search by (name, assetId, description, etc.): ")
        query = input("Search query: ")
        print()
        found = False
        for asset in assets:
            found = assetSearch(asset, True, found)
        if not found:
            print("Not found!\n")

    elif command.lower() == "classes":
        class_dict = {}
        class_count = 0
        for asset in assets:
            for classes in asset.get("classList"):
                if classes.get("name") not in class_dict:
                    class_count += 1
                class_dict.setdefault(classes.get("name"), []).append(asset.get("name"))
        print("Number of classes: " + str(class_count) + "\n")
        for keys in class_dict:
            values = class_dict.get(keys)
            print(str(keys) + ": " + ', '.join(values))

    elif command.lower() == "tree":
        parent = input("Input an asset id: ")
        print()
        print(parent)
#        tree_dict = {}
        for asset in assets:
            if asset.get("parentId") == int(parent):
                print("  |-" + str(asset.get("assetId")))
#            if asset.get("assetId") == int(parent):
#                childlist = getChildren(asset)
#                while childlist != []:
#                    for children in childlist:
#                        childlist = getChildren(children)

    else:
        print("Command not found!\n")





