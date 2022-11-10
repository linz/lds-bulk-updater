# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:55:15 2022

@author: PKhosla
"""
import unittest
import os
import sys
from io import StringIO
from dotenv import load_dotenv
from bulkdata_updater import bulkdata_updater

load_dotenv()

sys.path.append("../")


class TestCaseBulkdataUpdaterUpdFile(unittest.TestCase):
    """
    To test the API calls at various stages.
    """

    def __init__(self, *args, **kwargs):
        super(TestCaseBulkdataUpdaterUpdFile, self).__init__(*args, **kwargs)

    def setUp(self):
        """
        Get reference to config object
        """
        self.layer_id = os.getenv("Layer")
        self.domain = os.getenv("DOMAIN")
        self.e_api_key = os.getenv("E_API_KEY")
        self.api_key = os.getenv("API_KEY")

    def test_get_draft_id_fail(self):
        """
        Test with the wrong API Key
        """
        self.assertRaises(SystemExit, bulkdata_updater.get_draft_id, self.layer_id, self.e_api_key, self.domain)

    def test_get_draft_id(self):
        """
        Test with the correct API Key
        """
        global DRAFT_ID
        DRAFT_ID = bulkdata_updater.get_draft_id(self.layer_id, self.api_key, self.domain)
        self.assertTrue(isinstance(DRAFT_ID, int))

    def test_trigger_import_fail(self):
        """
        Test with the wrong API Key
        """
        self.assertRaises(SystemExit, bulkdata_updater.trigger_import, self.layer_id, DRAFT_ID, self.e_api_key, self.domain)

    def test_publish_layer(self):
        """
        Test with the correct API Key
        """
        expected_output = "data updated successfully\n"
        captured_output = StringIO()  # Create StringIO object
        sys.stdout = captured_output  #  and redirect stdout.
        bulkdata_updater.publish_layer(self.layer_id, DRAFT_ID, self.api_key, self.domain)
        sys.stdout = sys.__stdout__  # Reset redirect.
        print("Captured", captured_output.getvalue())
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_publish_layer_fail(self):
        """
        Test with the wrong API Key
        """
        expected_output = "Failed to make an Update\n"
        captured_output = StringIO()  # Create StringIO object
        sys.stdout = captured_output  #  and redirect stdout.
        bulkdata_updater.publish_layer(self.layer_id, DRAFT_ID, self.e_api_key, self.domain)
        sys.stdout = sys.__stdout__  # Reset redirect.
        print("Captured", captured_output.getvalue())
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
