from aiogram import F, Router
from aiogram.enums import ContentType
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import keyboards as kb

router = Router()


# Define states
class Form(StatesGroup):
    deposit = State()
    withdrawal = State()
    extension = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Приветствую тебя в нашем боте!",
                         reply_markup=kb.main_menu)

@router.message(F.text == "В главное меню")
async def cmd_start(message: Message):
    await message.answer("Выберите пункт меню:",
                         reply_markup=kb.main_menu)

@router.message(F.text == "Условия вклада")
async def show_deposit_conditions(message: Message):
    await message.answer(text="Что вас интересует?", reply_markup=kb.deposit_conditions_menu)


@router.message(F.text == "Этапы сотрудничества")
async def show_cooperation_stages(message: Message):
    await message.answer("Что вас интересует?", reply_markup=kb.cooperation_stages_menu)


@router.message(F.text == "По вкладу")
async def show_deposit_cooperation_stages(message: Message):
    answer = ("Этапы сотрудничества:\n 1.Cвязь с представителем\n"+
              " 2. Подписание электронного договора\n 3. Уточнение деталей\n"+
              " 4. Перечисление средств\n 5. Отслеживание статуса)")
    await message.answer(answer, reply_markup=kb.main_menu)
@router.message(F.text == "По выводу")
async def show_withdraw_cooperation_stages(message: Message):
    answer = ("Этапы сотрудничества:\n 1.Cвязь с представителем\n" +
              " 2. Подписание электронного договора\n 3. Уточнение деталей\n" +
              " 4. Перечисление средств\n 5. Отслеживание статуса)")
    await message.answer(answer, reply_markup=kb.main_menu)


@router.message(F.text == "Зарубежные переводы")
async def show_foreign_transfers(message: Message):
    await message.answer("Выберите тип перевода:", reply_markup=kb.foreign_transfers_menu)

@router.message(F.text == "На карту")
async def show_withdraw_cooperation_stages(message: Message):
    await message.answer("В разработке", reply_markup=kb.main_menu)
@router.message(F.text == "Оплата интернет услуг")
async def show_withdraw_cooperation_stages(message: Message):
    await message.answer("В разработке", reply_markup=kb.main_menu)

@router.message(F.text == "Баланс счета")
async def show_deposit_application(message: Message, state: FSMContext):
    await message.answer("В разработке", reply_markup=kb.main_menu)

@router.message(F.text == "Заявка на внесение")
async def show_deposit_application(message: Message, state: FSMContext):
    await state.set_state(Form.deposit)
    await message.answer("В разработке", reply_markup=kb.main_menu)


@router.message(F.text == "Заявка на вывод")
async def show_deposit_application(message: Message, state: FSMContext):
    await state.set_state(Form.withdrawal)
    await message.answer("В разработке", reply_markup=kb.main_menu)


@router.message(F.text == "Заявка на продление срока")
async def show_deposit_application(message: Message, state: FSMContext):
    await state.set_state(Form.extension)
    await message.answer("В разработке", reply_markup=kb.main_menu)


# Callback handlers for inline buttons
@router.message(F.text == "Простой процент")
async def show_simple_interest_options(message: Message):
    await message.answer("Выберите", reply_markup=kb.simple_interest_menu)


@router.message(F.text == "Сложный процент")
async def show_compound_interest_options(message: Message):
    await message.answer("Выберите количество дней:", reply_markup=kb.compound_interest_menu)


@router.message(F.text == 'Объяснение процентов')
async def show_interest_explanation(message: Message):
    await message.answer("О чём бы вы хотели узнать?", reply_markup=kb.explanation_menu)

@router.message(F.text == 'Подробные условия (PDF)')
async def show_interest_explanation(message: Message):
    await message.answer_document("BQACAgIAAxkBAAICyGZl3b0sH0kIAkP8ZHgb1tmNAeFWAAK-RAACjX8xSyDI5NfBB274NQQ")
