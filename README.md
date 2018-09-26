#TwinThread Backend Coding Challenge

This is my interpretation of the backend coding challenge for TwinThread.  This program was written in Python due to the robust built-in JSON parser and the simple to use data manipulation properties featured.

  To use, simply type the command `./assetmanager.py` in the command line.  Internal commands are as follows:
| command         | results                                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| exit            |  closes the program                                                                                                                                                               |
| help            | returns a list of all valid commands                                                                                                                                              |
| list            | returns a list of all assets that have a critical status and returns a shortened version of asset info (assetId: name)                                                            |
| list complete   | returns a list of all assets that have a critical status and returns a complete detail of given assets                                                                            |
| search          | returns a list of all assets that match the given search parameters (name, assetId, description, etc.) as well as completely match the search query.  Returns in shortened form.  |
| search complete | returns a list of all assets that match the given search parameters  (name, assetId, description, etc.) as well as completely match the  search query.  Returns in complete form. |
| classes         | returns the number of distinct classes contained within assets, then returns each class and the list of asset names that contain said class                                       |
| tree            | returns a hierarchy of an asset and its recursive children                                                                                                                        |

Thanks!