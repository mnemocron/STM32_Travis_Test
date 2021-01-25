################################################################################

# Automatically-generated file. Do not edit!

################################################################################



-include ../makefile.init



RM := rm -rf



# All of the sources participating in the build are defined here

-include sources.mk

-include Drivers/STM32F1xx_HAL_Driver/Src/subdir.mk

-include Core/Startup/subdir.mk

-include Core/Src/subdir.mk

-include subdir.mk

-include objects.mk



ifneq ($(MAKECMDGOALS),clean)

ifneq ($(strip $(S_DEPS)),)

-include $(S_DEPS)

endif

ifneq ($(strip $(S_UPPER_DEPS)),)

-include $(S_UPPER_DEPS)

endif

ifneq ($(strip $(C_DEPS)),)

-include $(C_DEPS)

endif

endif



-include ../makefile.defs



BUILD_ARTIFACT_NAME := Travis_CI_Test_f103rb

BUILD_ARTIFACT_EXTENSION := elf

BUILD_ARTIFACT_PREFIX := 

BUILD_ARTIFACT := $(BUILD_ARTIFACT_PREFIX)$(BUILD_ARTIFACT_NAME).$(BUILD_ARTIFACT_EXTENSION)



# Add inputs and outputs from these tool invocations to the build variables 

EXECUTABLES += \

Travis_CI_Test_f103rb.elf \



SIZE_OUTPUT += \

default.size.stdout \



OBJDUMP_LIST += \

Travis_CI_Test_f103rb.list \



OBJCOPY_BIN += \

Travis_CI_Test_f103rb.bin \





# All Target

all: main-build



# Main-build Target

main-build: Travis_CI_Test_f103rb.elf secondary-outputs



# Tool invocations

Travis_CI_Test_f103rb.elf: $(OBJS) $(USER_OBJS) ../STM32F103RBTX_FLASH.ld

	arm-none-eabi-gcc -o "Travis_CI_Test_f103rb.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m3 -T"../STM32F103RBTX_FLASH.ld" --specs=nosys.specs -Wl,-Map="Travis_CI_Test_f103rb.map" -Wl,--gc-sections -static --specs=nano.specs -mfloat-abi=soft -mthumb -Wl,--start-group -lc -lm -Wl,--end-group

	@echo 'Finished building target: $@'

	@echo ' '



default.size.stdout: $(EXECUTABLES)

	arm-none-eabi-size  $(EXECUTABLES)

	@echo 'Finished building: $@'

	@echo ' '



Travis_CI_Test_f103rb.list: $(EXECUTABLES)

	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "Travis_CI_Test_f103rb.list"

	@echo 'Finished building: $@'

	@echo ' '



Travis_CI_Test_f103rb.bin: $(EXECUTABLES)

	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "Travis_CI_Test_f103rb.bin"

	@echo 'Finished building: $@'

	@echo ' '



# Other Targets

clean:

	-$(RM) *

	-@echo ' '



secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_BIN)



fail-specified-linker-script-missing:

	@echo 'Error: Cannot find the specified linker script. Check the linker settings in the build configuration.'

	@exit 2



warn-no-linker-script-specified:

	@echo 'Warning: No linker script specified. Check the linker settings in the build configuration.'



.PHONY: all clean dependents fail-specified-linker-script-missing warn-no-linker-script-specified

.SECONDARY:



-include ../makefile.targets

