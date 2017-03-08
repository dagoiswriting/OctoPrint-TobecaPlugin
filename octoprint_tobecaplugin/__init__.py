# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started.

import octoprint.plugin

class TobecaPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("Plugin Tobeca!")
        
    def get_assets(self):
      return dict(
         js=["js/tobecaplugin.js"]
      )

    def get_update_information(self):
        return dict(
            systemcommandeditor=dict(
                displayName="Tobeca Plugin",
                displayVersion=self._plugin_version,

                # version check: github repository
                type="github_release",
                user="tobeca",
                repo="OctoPrint-TobecaPlugin",
                current=self._plugin_version,

                # update method: pip
                pip="https://github.com/tobeca/OctoPrint-TobecaPlugin/archive/{target_version}.zip"
            )
        )

      
        

# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Tobeca"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = TobecaPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }