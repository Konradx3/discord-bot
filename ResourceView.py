import discord
from ResourceDropdown import ResourceDropdown
from TierDropdown import TierDropdown
from EnchantDropdown import EnchantDropdown
from AlbionDataAPI import AlbionDataAPI


class ResourceView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.selection = {}
        self.resource_dropdown = ResourceDropdown()
        self.tier_dropdown = TierDropdown()
        self.enchant_dropdown = EnchantDropdown()
        self.add_item(self.resource_dropdown)
        self.add_item(self.tier_dropdown)
        self.add_item(self.enchant_dropdown)

    async def update_selection(self, category, value, options):
        label = next((option.label for option in options if option.value == value), value)
        self.selection[category] = {'value': value, 'label': label}

    async def check_complete(self, interaction: discord.Interaction):
        resource_value = self.resource_dropdown.values
        tier_value = self.tier_dropdown.values
        enchant_value = self.enchant_dropdown.values

        if all(category in self.selection for category in ['resource', 'tier', 'enchant']):
            resource_label = self.selection['resource']['label']
            tier_label = self.selection['tier']['label']
            enchant_label = self.selection['enchant']['label']

            albion_api = AlbionDataAPI(resource_value, tier_value, enchant_value)
            response = albion_api.get_resource_prices()

            if 'error' in response:
                message = response['error']
            else:
                table_header = "| Miasto             |  Cena sprzedaży  |  Cena kupna  |\n"
                table_header += "|--------------------|------------------|--------------|\n"

                table_rows = ""
                for item in response:
                    city = item['city']
                    sell_price_min = item['sell_price_min']
                    buy_price_max = item['buy_price_max']
                    table_rows += f"| {city:<14}     |  {sell_price_min:<14}  |  {buy_price_max:<10}  |\n"

                message = f'Cena {resource_label} {tier_label}.{enchant_label} we wszystkich miastach:\n```\n{table_header}{table_rows}```'

            await interaction.response.send_message(content=message)
        else:
            await interaction.response.defer()
