odoo.define('hsp.BasicRenderer', function (require) {
    "use strict";
    
    /**
     * The BasicRenderer is an abstract class designed to share code between all
     * views that uses a BasicModel. The main goal is to keep track of all field
     * widgets, and properly destroy them whenever a rerender is done. The widgets
     * and modifiers updates mechanism is also shared in the BasicRenderer.
     */
    var AbstractRenderer = require('web.AbstractRenderer');
    var config = require('web.config');
    var core = require('web.core');
    var dom = require('web.dom');
    var widgetRegistry = require('web.widget_registry');
    var BasicRenderer = require('web.BasicRenderer');
    
    
    var qweb = core.qweb;
    BasicRenderer.include({
            /**
     * Add a tooltip on a $node, depending on a field description
     *
     * @param {FieldWidget} widget
     * @param {$node} $node
     */
    _addFieldTooltip: function (widget, $node) {
        // optional argument $node, the jQuery element on which the tooltip
        // should be attached if not given, the tooltip is attached on the
        // widget's $el
        // console.log(widget.record.model)
        // console.log(widget)
        // console.log(widget.record.context.lang)
        $node = $node.length ? $node : widget.$el;
        $node.tooltip({
            title: function () {
                return qweb.render('hsp.WidgetLabel.tooltip', {
                    debug: config.isDebug(),
                    widget: widget,
                });
            },
            delay: { "show": 0, "hide": 20000 }
        });
    },
    })
});
    