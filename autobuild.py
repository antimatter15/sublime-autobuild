from os.path import splitext, basename, dirname, join
import sublime_plugin


class AutoBuild(sublime_plugin.EventListener):
    def on_post_save(self, view):
        file_path = view.file_name()
        working_dir = dirname(file_path)
        file_name, file_type = splitext(basename(file_path))
        file_types = [".coffee", ".less", ".sass", ".scss"]
        if file_type in file_types:
            view.window().run_command("build")
            view.window().run_command("hide_panel")
        else:
            return []
