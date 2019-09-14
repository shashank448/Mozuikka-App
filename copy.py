def setup_player(self):
    try:
        self.my_player = Player.Player()
        if self.my_player.get_db_status():
            messagebox.showinfo("Success !", "Connected Succesfully to the DB")

        else:
            raise Exception("Sorry !,you cannot save or load the favourites !!!")
    except Exception as ex:
        print("DB_Error", ex)
        messagebox.showerror("DB Error !", ex)
        self.Button9.configure(state="disabled")
        self.Button10.configure(state="disabled")
        self.Button11.configure(state="disabled")

    self.vol_scale.configure(from_=0, to=100, command=self.change_volume)
    self.vol_scale.set(50)

    self.addSongsToPlayListButton.configure(command=self.add_song)
    self.deleteSongsFromPlaylistButton.configure(command=self.remove_song)
    self.playButton.configure(command=self.play_song)
    self.stopButton.configure(command=self.stop_song)
    self.pauseButton.configure(command=self.pause_song)
    self.playList.configure(font="Vivaldi 12")
    self.playList.bind("<Double-1>", self.list_double_click)
    img = tk.PhotoImage(file="C:/Users/user/Desktop/sih/Untitled.png")
    self.top.iconphoto(self.top, img)
    self.top.title("MOUZIKKA - Dance to the rhythm of your heart ..!!")
    self.top.protocol("WM_DELETE_WINDOW", self.closewindow)
    self.isPaused = False
    self.isPlaying = False
    self.previousButton.configure(command=self.previous_song)
    self.prev_song = []


def previous_song(self):
    if self.isPlaying == True:
        self.song_name = self.prev_song[-1]
    if self.isPaused == True:
        self.song_name = self.prev_song[0]

    print(self.song_name)
    self.show_song_details()
    self.my_player.play_song()
    self.change_volume(self.vol_scale.get())
    self.isPlaying = True
    if len(self.prev_song) < 2:
        self.prev_song = [self.song_name] + self.prev_song
        # print(self.prev_song)
    else:
        self.prev_song.pop()
        self.prev_song = [self.song_name] + self.prev_song
        # print(self.prev_song)


def show_song_details(self):
    self.song_length = self.my_player.get_song_length(self.song_name)
    min, sec = divmod(self.song_length, 60)
    min = round(min)
    sec = round(sec)
    self.songTotalDuration.configure(text=str(min) + ':' + str(sec))
    self.songTimePassed.configure(text="0:0")
    ext_index = self.song_name.rfind(".")
    song_name_str = self.song_name[0:ext_index]
    if (len(song_name_str) > 14):
        song_name_str = song_name_str[0:14] + "..."
    self.songName.configure(text=song_name_str)


def play_song(self):
    self.sel_song_index_tuple = self.playList.curselection()
    try:
        if len(self.sel_song_index_tuple) == 0:
            raise NoSongSelectedError("please select a song to play")
        self.song_name = self.playList.get(self.sel_song_index_tuple[0])
        self.show_song_details()
        self.my_player.play_song()
        self.change_volume(self.vol_scale.get())
        self.isPlaying = True
        # self.prev_song=" "
        # if self.prev_song != self.song_name:
        #   self.prev_song=self.song_name
        # else:
        if len(self.prev_song) < 2:
            self.prev_song = [self.song_name] + self.prev_song
            print(self.prev_song)
        else:
            self.prev_song.pop()
            self.prev_song = [self.song_name] + self.prev_song
            print(self.prev_song)



    except (NoSongSelectedError) as ex1:
        messagebox.showerror("Error..!", ex1)
