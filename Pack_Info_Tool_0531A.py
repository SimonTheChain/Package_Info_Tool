#!/usr/bin/python
# -*- coding: utf-8 -*-

# Package Info Tool
#
# Version: 0531A
#
# Author: Simon Lachaîne


import os
import sys
import time

from PyQt4 import QtCore, QtGui

import languages_complete as languages_list
import pack_info_ui as main_frame


def create_list(subject_lst, dict):
    """
    Creates a list from the dictionary of languages
    :return: list of language initials with their name
    """
    subject_lst = []
    for i in dict:
        subject_lst.append(i + ": " + dict[i])
    subject_lst.sort()
    return subject_lst


class CreateFile(QtCore.QThread):

    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        pass


class PackInfoApp(QtGui.QMainWindow, main_frame.Ui_PackInfo):
    def __init__(self, parent=None):
        super(PackInfoApp, self).__init__(parent)

        self.create_file_thread = CreateFile()

        list_of_languages = create_list("language_lst", languages_list.languages)

        self.setupUi(self)

        # metadata

        # feature

        self.feat_spoken.clear()
        self.feat_spoken.addItems(list_of_languages)
        self.feat_spoken.currentIndexChanged.connect(self.set_feat_audio)
        index_feature_audio = self.feat_spoken.findText("en-CA: English (Canada)",
                                                        QtCore.Qt.MatchFixedString)
        self.feat_spoken.setCurrentIndex(index_feature_audio)

        self.feat_burnt_subs_locale.clear()
        self.feat_burnt_subs_locale.addItems(list_of_languages)
        self.feat_burnt_subs_locale.currentIndexChanged.connect(self.set_feat_burnt_subs_locale)
        index_feat_burnt_subs_locale = self.feat_burnt_subs_locale.findText("en-CA: English (Canada)",
                                                                            QtCore.Qt.MatchFixedString)
        self.feat_burnt_subs_locale.setCurrentIndex(index_feat_burnt_subs_locale)

        self.feat_burnt_narr_locale.clear()
        self.feat_burnt_narr_locale.addItems(list_of_languages)
        self.feat_burnt_narr_locale.currentIndexChanged.connect(self.set_feat_burnt_narr_locale)
        index_feat_burnt_narr_locale = self.feat_burnt_narr_locale.findText("en-CA: English (Canada)",
                                                                            QtCore.Qt.MatchFixedString)
        self.feat_burnt_narr_locale.setCurrentIndex(index_feat_burnt_narr_locale)

        self.feat_alt_audio_locale.clear()
        self.feat_alt_audio_locale.addItems(list_of_languages)
        self.feat_alt_audio_locale.currentIndexChanged.connect(self.set_feat_alt_audio_locale)
        index_feat_alt_audio_locale = self.feat_alt_audio_locale.findText("en-CA: English (Canada)",
                                                                            QtCore.Qt.MatchFixedString)
        self.feat_alt_audio_locale.setCurrentIndex(index_feat_alt_audio_locale)

        # trailer

        self.show()

    def set_feat_audio(self):
        pass

    def set_feat_burnt_subs_locale(self):
        pass

    def set_feat_burnt_narr_locale(self):
        pass

    def set_feat_alt_audio_locale(self):
        pass


def main():
    app = QtGui.QApplication(sys.argv)
    gui = PackInfoApp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
