
/** @odoo-module **/

import { Component, useState } from 'owl';

class StockRequestProgress extends Component {
    setup() {
        // Estado que rastrea el progreso de la solicitud
        this.state = useState({
            steps: [
                { label: "Warehouse", completed: false },
                { label: "Location", completed: false },
                { label: "Products", completed: false },
                { label: "Route", completed: false },
            ]
        });

        this.checkProgress();
    }

    checkProgress() {
        const warehouseField = this.el.querySelector('input[name="warehouse_id"]');
        const locationField = this.el.querySelector('input[name="location_id"]');
        const productsField = this.el.querySelector('input[name="stock_request_ids"]');
        const routeField = this.el.querySelector('input[name="route_id"]');

        this.state.steps[0].completed = !!warehouseField.value;
        this.state.steps[1].completed = !!locationField.value;
        this.state.steps[2].completed = !!productsField.value;
        this.state.steps[3].completed = !!routeField.value;

        if (this.state.steps[0].completed) {
            locationField.removeAttribute('disabled');
        }
        if (this.state.steps[1].completed) {
            productsField.removeAttribute('disabled');
        }
        if (this.state.steps[2].completed) {
            routeField.removeAttribute('disabled');
        }
    }

    static template = "custom_stock_request_extension.StockRequestProgress";
}

export default StockRequestProgress;
