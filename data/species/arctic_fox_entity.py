from entities import SpeciesEntity, SpeciesAbilitiesBonus, SpeciesAbilityBonus
import constants.species
import constants.abilities


SPECIES_ENTITY_ARCTIC_FOX = SpeciesEntity(
    key=constants.species.Species.ARCTIC_FOX,
    description=(
        'Песцы один из двух видов невеличек чьи государства находятся на суровом севере известной территории Риарги. '
        'Государство Жромба, обычно незаметна на мировой политической арены, так как они <ins>живут войной с суровой '
        'местностью</ins>, они немного численны, но они заняли нишу в которой кроме них уместились только пингвины. '
        'В их землях распространена веры в бога вечной зимы Рахака, который учит выживанию в вечной мерзлоте и терпению.'
    ),
    size_description=(
        'Рост крепких и вертких песцов, в среднем составляет **65-70 сантиметров**.<br>'
        '**Размер: <ins>Средний</ins>**'
    ),
    speed_in_meters=20,
    languages_description='Вы можете говорить, читать и писать на **Общем** и на **Жроском**.',
    additional_features=[
        'Опытный охотник',
        'Устойчивость к холоду',
    ],
    image_path='./images/arctic_fox.png',
    species_abilities_bonuses=[
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.DEXTERITY, bonus=2),
                SpeciesAbilityBonus(key=constants.abilities.Ability.WISDOM, bonus=1),
            ],
        ),
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.DEXTERITY, bonus=1),
                SpeciesAbilityBonus(key=constants.abilities.Ability.WISDOM, bonus=2),
            ],
        ),
    ]
)
