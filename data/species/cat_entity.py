from entities import SpeciesEntity, SpeciesAbilitiesBonus, SpeciesAbilityBonus
import constants.species
import constants.abilities


SPECIES_ENTITY_CAT = SpeciesEntity(
    key=constants.species.Species.CAT,
    description=(
        'Коты, пожалуй самая ненавистный вид невеличек на Риарге, их бесперерывные военные компании направленные '
        'против двух государств, <ins>настроили всех как против их Империи, так и против обычных представителей</ins> этого вида, '
        'хотя далеко не все этого заслуживают, хотя национализм котам вполне присущ. <ins>Они ловки и харизматичны</ins>, '
        'что делает их хорошими воинами и магами, хотя магии учатся коты ходящие на двух лапах либо за большие '
        'деньги либо за пределами Империи. Верят, что они Смотрящие в щель.'
    ),
    size_description=(
        'Вы средних размеров среди невеличек около **60-65 сантиметров**.<br>'
        '**Размер: <ins>Средний</ins>**'
    ),
    speed_in_meters=20,
    languages_description='Вы можете говорить, читать и писать на **Общем** и на **Великоимперском**.',
    additional_features=[
        'Чувство опасности',
        'Зрение в темноте',
    ],
    image_path='./images/cat.png',
    species_abilities_bonuses=[
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.DEXTERITY, bonus=2),
                SpeciesAbilityBonus(key=constants.abilities.Ability.CHARISMA, bonus=1),
            ],
        ),
    ]
)
