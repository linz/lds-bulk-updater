# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:56:15 2022

@author: PKhosla
"""

import unittest
import sys
import os
import logging
from bulkdata_updater import bulkdata_updater
from bulkdata_updater import log

sys.path.append("../")


class TestBulkdataUpdaterConfig(unittest.TestCase):
    """
    Congig file Tests
    """

    def test_read_config(self):
        """
        Ensure all required properties are present in
        config template
        """

        config_file = os.path.join(os.sep, os.getcwd(), "../bulkdata_updater/config_template.yaml")
        config = bulkdata_updater.ConfigReader(config_file)
        self.assertEqual(config.api_key, "key <ADMIN API KEY>")
        self.assertEqual(config.domain, "<Data Service Domain>")
        self.assertEqual(config.layers, "<Layers to Process>")

    def test_config_get_cwd(self):
        """
        Tests FileNotFoundError exception.
        """
        self.assertRaises(FileNotFoundError, bulkdata_updater.ConfigReader, None)


class TestMetadataLog(unittest.TestCase):
    """
    Log Tests
    """

    def test_log(self):
        """
        test a logging instance is returned
        """

        logger = log.conf_logging("root")
        self.assertIsInstance(logger, logging.Logger)


if __name__ == "__main__":
    unittest.main()
