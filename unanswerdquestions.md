# Question 1

__**May June 2025 Region 3**__

A collector needs a video library system for a collection of videos stored on 4K Blu-ray discs, standard Blu-ray discs, DVD, or as digital downloads. 

The two-dimensional (2D) array `Video[]` is used to store, for each video item, the title, the format of the video (4K Blu-ray disc, standard Blu-ray disc, DVD, or digital download), the year it was released stored as a string and a storage code to represent where the video can be found in the collection, for example:

- `Video[1,1]` is "Macbeth"
- `Video[1,2]` is "digital download"
- `Video[1,3]` is "2015"
- `Video[1,4]` is "DG276"

The two-dimensional (2D) array `Results[]` is used to store the results of a search to find a specific video. 

The search uses the video title, and if the video is found, its data is copied from the array `Video[]` to the array `Results[]`. 

The search continues and if other videos with the same title are found, this data is also copied to the array `Results[]`. 

The search ends when the end of the data is reached.

__Write a program that meets the following requirements:__
- The video library array needs to be initialised with the null string (""), allowing for up to 10 000 records. The array `Results[]` must be initialised before every search with the null string and must be able to hold up to 20 search results with the same title.
- Create a menu to add a new video to the library to search for an existing video by title, or to stop, with validation of the input.
- When the user enters a new video, the following data is stored in the first available location of the relevant array:
  - video title
  - format (4K Blu-ray disc, standard Blu-ray disc, DVD, digital download)
  - year of release as string
  - storage code.
- Allow input of data for another video if required.
- When searching for an existing video, if a match is found, transfer all the data for that video into the array `Results[]`, and continue to search until all videos with the same title have been found.
- Output the results from the array `Results[]`
- If the video title is not found, output a suitable message.
- The system returns to the menu after completing the input or the output, until the user chooses to stop.

You must use **pseudocode or program code**

You do not need to declare any arrays, variables or constants. 

You may assume that this has already been done.

All inputs and outputs must contain suitable messages.
