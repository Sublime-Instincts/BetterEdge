import json
import sublime
import mdpopups
import sublime_plugin

_css = """
.betteredge_popup {
    margin: -4rem 0.5rem 0 0.5rem;
    font-family: system;
    line-height: 0.1;
}
.autocomplete_value {
    line-height: 0.1;
    margin-bottom: 0.1rem;
}
"""

betteredge_popup_content = """
<style>{}</style>
<div class="betteredge_popup">
    <h6 class="autocomplete_value">{}</h6>
    <p class="docs">{}</p>
    {}{}
</div>
"""


class BetterEdgeCompletionsListener(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):

        if not view.match_selector(locations[0] - 1, "text.html.edge"):
            return

        completions_data = json.loads(sublime.load_resource(sublime.find_resources("edge_completions_data.json")[0]))

        return (
            [
                sublime.CompletionItem(
                    trigger=key,
                    completion="{}()".format(key),
                    annotation=value.get("annotation"),
                    kind=(sublime.KIND_ID_NAMESPACE, "h", "Helper"),
                    details="<a href='{}'>documentation</a>".format(
                        sublime.command_url("better_edge_popup", { "key": key, "value": value })
                    )
                )
                for key, value in completions_data.items()
            ]
        )

class BetterEdgePopupCommand(sublime_plugin.TextCommand):

    def run(self, edit, key, value):
        edge_language_highlight = mdpopups.syntax_highlight(
            view = self.view,
            src = value["code_sample"],
            language = "edge",
            language_map = {
                "edge": (("edge",), ("BetterEdge/resources/syntax/HTML (Edge)",))
            }
        )

        argument_description = ""

        if value.get("arguments"):
            for arg in value["arguments"]:
                argument_description += "<p>@arg <code>{}</code> {}</p>".format(
                    arg["type"], arg["description"]
                )

        arguments = """<div class="arguments">{}</div>""".format(argument_description)

        mdpopups.show_popup(
            view = self.view,
            content = betteredge_popup_content.format(
                _css, key, value["description"], edge_language_highlight, arguments
            ),
            flags=sublime.COOPERATE_WITH_AUTO_COMPLETE,
            max_width=500
        )
