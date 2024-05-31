from entities import SpeciesEntity, SpeciesAbilitiesBonus, SpeciesAbilityBonus
import constants.species
import constants.abilities


SPECIES_ENTITY_PARROT = SpeciesEntity(
    key=constants.species.Species.PARROT,
    description=(
        'Попугаи  - это либо умирающая нация, либо гонимые беженцы из умирающей страны, нашедшие приют только '
        'на каменистом острове. Несмотря на вышеперечисленное , это все ещё один из самых многочисленных видов '
        'на Риарге. Попугаи известны своей харизмой, которая <ins>позволяет им быть лучшими магами и дипломатами</ins>, за '
        'что они <ins>невероятно ценятся</ins>, хотя и это <ins>не помогло им обрести дом</ins> в другом государстве. Религия '
        'восходит либо к Десятерым защитникам, либо богам пор года.'
    ),
    size_description=(
        'Вы чуть меньше средних размеров среди невеличек около **50-55 сантиметров**.<br>'
        '**Размер: <ins>Средний</ins>**'
    ),
    speed_in_meters=15,
    languages_description='Вы можете говорить, читать и писать на **Общем** и на **Гиракском**.',
    additional_features=[
        'Способность к полету без доспехов',
        'Повышенная внимательность',
    ],
    image_path='./images/parrot.png',
    species_abilities_bonuses=[
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.CHARISMA, bonus=2),
                SpeciesAbilityBonus(key=constants.abilities.Ability.DEXTERITY, bonus=1),
            ],
        ),
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.STRENGTH, bonus=1),
                SpeciesAbilityBonus(key=constants.abilities.Ability.DEXTERITY, bonus=1),
                SpeciesAbilityBonus(key=constants.abilities.Ability.CHARISMA, bonus=1),
            ],
        ),
    ]
)
